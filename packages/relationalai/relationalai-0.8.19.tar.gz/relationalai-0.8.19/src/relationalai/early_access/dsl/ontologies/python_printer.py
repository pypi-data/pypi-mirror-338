import typing
from collections import defaultdict
from typing import TypeVar

from relationalai.early_access.dsl import Model, EntityType, ExternalRelation
from relationalai.early_access.dsl.core.types import Type
from relationalai.early_access.dsl.core.types.standard import standard_value_types
from relationalai.early_access.dsl.core.utils import camel_to_snake
from relationalai.early_access.dsl.ontologies.constraints import Mandatory, Unique
from relationalai.early_access.dsl.ontologies.roles import AbstractRole
from relationalai.early_access.dsl.ontologies.subtyping import SubtypeConstraint, SubtypeArrow, \
    ExclusiveSubtypeConstraint, InclusiveSubtypeConstraint
from relationalai.early_access.metamodel.util import Printer

# Define a generic type variable constrained to SubtypeConstraint or its subclasses
T = TypeVar("T", bound=SubtypeConstraint)

class PythonPrinter(Printer):

    def to_python_string(self, model: Model) -> None:
        self._print_nl("import relationalai.early_access.dsl as rai")
        self._nl()

        self._print_nl(f"model = rai.Model(name='{model.name}', is_primary={model.is_primary})")
        self._print_nl("Concept = model.concept")
        self._print_nl("Entity = model.entity_type")
        self._print_nl("SubtypeArrow = model.subtype_arrow")
        self._print_nl("Relationship = model.relationship")
        self._print_nl("RefScheme = model.ref_scheme")
        self._print_nl("ExternalRelation = model.external_relation")

        self._nl()
        self._handle_value_types(model)

        self._nl()
        self._handle_entity_types(model)

        self._nl()
        self._handle_relationships(model)

        self._handle_composite_reference_schemas(model)

        self._nl()
        self._handle_external_relations(model)

        # TODO: handle Account.add_instance('Exchange') etc.

    def _handle_value_types(self, model: Model) -> None:
        for vt in model.value_types():
            self._print_nl(f"{vt.name()} = Concept('{vt.name()}', {', '.join(self._get_type(t) for t in vt._types)})")

    def _handle_entity_types(self, model: Model) -> None:
        subtype_arrows_by_type = self._group_subtype_arrows_by_type(model)
        inclusive_subtype_constraints_by_type = self._get_inclusive_subtype_constraints_by_type(model)
        exclusive_subtype_constraints_by_type = self._get_exclusive_subtype_constraints_by_type(model)

        for et in model.entity_types():
            name = et.name()
            if len(et.domain()) > 0:
                domain = ", ".join(self._get_type(t) for t in et.domain())
                self._print_nl(f"{name} = Entity('{name}', {domain})")
            else:
                self._print_nl(f"{name} = Entity('{name}')")
                self._handle_subtype_arrows(et,
                                            subtype_arrows_by_type.get(et, set()),
                                            inclusive_subtype_constraints_by_type.get(et, set()),
                                            exclusive_subtype_constraints_by_type.get(et, set()))

    def _handle_subtype_arrows(self, et: EntityType, subtype_arrows, inclusive_subtype_constraints,
                               exclusive_subtype_constraints) -> None:
        name = et.name()

        # Common elements in both sets
        common_constraints = inclusive_subtype_constraints & exclusive_subtype_constraints
        if len(common_constraints) > 0:
            for c in common_constraints:
                self._print_nl(f"SubtypeArrow({name}, [{', '.join(self._get_type(a.start) for a in c.arrows)}], "
                               f"exclusive=True, inclusive=True)")

        # Only in inclusive (but not in exclusive)
        only_inclusive_constraints = inclusive_subtype_constraints - exclusive_subtype_constraints
        if len(only_inclusive_constraints) > 0:
            for c in only_inclusive_constraints:
                self._print_nl(f"SubtypeArrow({name}, [{', '.join(self._get_type(a.start) for a in c.arrows)}], "
                               f"inclusive=True)")

        # Only in exclusive (but not in inclusive)
        only_exclusive_constraints = exclusive_subtype_constraints - inclusive_subtype_constraints
        if len(only_exclusive_constraints) > 0:
            for c in only_exclusive_constraints:
                self._print_nl(f"SubtypeArrow({name}, [{', '.join(self._get_type(a.start) for a in c.arrows)}], "
                               f"exclusive=True)")

        # Get all arrows from both inclusive and exclusive constraints
        all_arrows_in_constraints = {a for c in inclusive_subtype_constraints for a in c.arrows} | \
                                    {a for c in exclusive_subtype_constraints for a in c.arrows}

        # Subtract the arrows in constraints from subtype_arrows
        remaining_constraints = subtype_arrows - all_arrows_in_constraints
        if len(remaining_constraints) > 0:
            for c in remaining_constraints:
                self._print_nl(f"SubtypeArrow({name}, [{', '.join(self._get_type(a.start) for a in c.arrows)}])")

    def _handle_relationships(self, model: Model) -> None:
        unique_roles = self._get_unique_roles(model)
        mandatory_roles = self._get_mandatory_roles(model)
        internal_preferred_identifier_roles = self._get_internal_preferred_identifier_roles(model)

        for rel in model.relationships():
            if not rel.is_subtype() and not rel.is_identifier():
                name = camel_to_snake(rel._name())
                self._print_nl(f"{name} = Relationship()")
                self._print_nl(f"with {name} as rel:")
                self._handle_relationship_roles(rel, mandatory_roles, unique_roles, internal_preferred_identifier_roles)
                self._handle_relationship_relations(rel)
                self._nl()

    def _handle_relationship_roles(self, rel, mandatory_roles, unique_roles, internal_preferred_identifier_roles):
        for i, r in enumerate(rel.roles()):
            self._indent_print_nl(1, f"rel.role({self._get_type(r.player())}"
                                     f"{self._print_if_not_empty('name', r.name())}"
                                     f"{self._print_if_true('unique', r in unique_roles)}"
                                     f"{self._print_if_true('mandatory', r in mandatory_roles)}"
                                     f"{self._print_if_true('primary_key', r in internal_preferred_identifier_roles)})")
            if r.prefix or r.postfix:
                elements = list(filter(None, [
                    self._print_first_if_not_empty('prefix', r.prefix),
                    self._print_first_if_not_empty('postfix', r.postfix)
                ]))
                self._indent_print_nl(1, f"rel.role_at({i}).verbalization({', '.join(elements)})")

    def _handle_relationship_relations(self, rel):
        for relation in rel.relations():
            if relation.reading():
                reading = relation.reading()

                num_roles = len(rel.roles())
                num_texts = len(reading.text_frags)

                elements = []

                for i in range(num_texts):
                    elements.append(f"rel.role_at({i})")  # Role first
                    elements.append(f"'{reading.text_frags[i]}'")  # Then text

                if num_roles > num_texts:
                    elements.append(f"rel.role_at({num_roles - 1})")  # Add last role if needed

                self._indent_print_nl(1, f"rel.relation({', '.join(elements)}"
                                         f"{self._print_if_not_empty('name', reading.rel_name)}"
                                         f"{self._print_if_true('functional', relation.signature().functional())})")

    def _handle_composite_reference_schemas(self, model: Model) -> None:
        for preferred_id in self._get_composite_preferred_identifiers(model):

            elements = []

            for role in preferred_id.roles():
                relationship = role.part_of

                # Find the matching relation where the 2nd role is `role`
                matching_relation = next(
                    (rel for rel in relationship.relations() if rel.reading().roles[1] == role),
                    None
                )

                if matching_relation:
                    roles = matching_relation.reading().roles
                    player_name = roles[0].player_type.name()
                    rel_name = matching_relation.rel_name()
                    elements.append(f"{player_name}.{rel_name}")
                else:
                    raise Exception(f"Could not find matching relation for role player {role.player().name()} "
                                    f"in relationship {relationship._name()}")

            self._print_nl(f"RefScheme({', '.join(elements)})")

    def _handle_external_relations(self, model: Model) -> None:
        external_relations = self._get_external_relations(model)
        for r in external_relations:
            self._print_nl(f"ExternalRelation('{r.rel_name()}', {', '.join(self._get_type(t) for t in r.signature().types())})")

    @staticmethod
    def _get_mandatory_roles(model: Model) -> set[AbstractRole]:
        return {c.role for c in model.constraints() if isinstance(c, Mandatory)}

    @staticmethod
    def _get_unique_roles(model: Model) -> set[AbstractRole]:
        return {role for c in model.constraints() if isinstance(c, Unique) and not c.is_preferred_identifier for role in c.roles()}

    @staticmethod
    def _get_internal_preferred_identifier_roles(model: Model) -> set[AbstractRole]:
        return {role for c in model.constraints() if isinstance(c, Unique) and c.is_preferred_identifier and len(c.roles()) == 1 for role in c.roles()}

    @staticmethod
    def _get_composite_preferred_identifiers(model: Model) -> set[Unique]:
        return {c for c in model.constraints() if isinstance(c, Unique) and c.is_preferred_identifier and len(c.roles()) > 1}

    @staticmethod
    def _get_type(t: Type) -> str:
        return f"rai.{t.name()}" if t.name() in standard_value_types else t.name()

    @staticmethod
    def _group_subtype_arrows_by_type(model: Model) -> dict[Type, set[SubtypeArrow]]:
        subtype_arrows_by_type = defaultdict(set)
        for a in model.subtype_arrows():
            subtype_arrows_by_type[a.end].add(a)
        return dict(subtype_arrows_by_type)

    @staticmethod
    def _get_subtype_constraints_by_type(model: Model, constraint_type: typing.Type[T]) -> dict[Type, set[T]]:
        constraints_by_type: dict[Type, set[T]] = defaultdict(set)

        for c in model.subtype_constraints():
            if isinstance(c, constraint_type):
                for a in c.arrows:
                    constraints_by_type[a.end].add(c)

        return dict(constraints_by_type)

    def _get_exclusive_subtype_constraints_by_type(self, model: Model) -> dict[Type, set[ExclusiveSubtypeConstraint]]:
        return self._get_subtype_constraints_by_type(model, ExclusiveSubtypeConstraint)

    def _get_inclusive_subtype_constraints_by_type(self, model: Model) -> dict[Type, set[InclusiveSubtypeConstraint]]:
        return self._get_subtype_constraints_by_type(model, InclusiveSubtypeConstraint)

    @staticmethod
    def _get_external_relations(model: Model) -> set[ExternalRelation]:
        return {r for r in model.relations() if isinstance(r, ExternalRelation)}

    @staticmethod
    def _print_if_not_empty(label: str, value: str) -> str:
        return f", {label}='{value}'" if value else ""

    @staticmethod
    def _print_first_if_not_empty(label: str, value: str) -> str:
        return f"{label}='{value}'" if value else ""

    @staticmethod
    def _print_if_true(label: str, value: bool) -> str:
        return f", {label}=True" if value else ""
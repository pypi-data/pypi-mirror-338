from typing import Optional

from relationalai.early_access.dsl.core.types import Type as CoreType
from relationalai.early_access.dsl.core.namespaces import Namespace
from relationalai.early_access.dsl.core.relations import Relation
from relationalai.early_access.dsl.core.utils import camel_to_snake


class Type(CoreType):

    # We can add relation components to a ConceptModule by invoking it
    # with arguments that interleave reading text with the Types used
    # to play various Roles
    #
    def __setattr__(self, key, value):
        if key in dir(self) and key not in self.__dict__:
            raise Exception(f"Cannot override method {key} of Type {self.name()} as an attribute.")
        else:
            if key[0] != '_':
                self._relations[key] = value
            return super().__setattr__(key, value)

    def __getitem__(self, key):
        return self.__dict__[key]

    def __init__(self, model, nm):
        super().__init__(nm)
        self._model = model
        self._relations = {}
        self._generated_namespace = None

    def relation(self, *args, name: Optional[str] = None, namespace: Optional[Namespace]=None, functional: bool=False) -> Relation:
        if len(args) == 1 and not isinstance(args[0], str):
            raise ValueError("For binary or higher order relations parameter 'args' should contain "
                            "Sequence of text fragments followed by Types.")
        self._generated_namespace = namespace
        relationship = self._model.relationship(*[self, *args], relation_name=name)
        rel = next(iter(relationship.relations()), None)
        if rel is not None:
            rel.signature().set_functional(functional)
            self.add_relation(rel)
            return rel
        raise Exception(f"Could not find relation for relationship {relationship.name()}")

    def add_relation(self, relation: Relation):
        self._relations[relation._relname] = relation
        self.__setattr__(relation._relname, relation)

    def generated_namespace(self):
        if self._generated_namespace is None:
            ename = camel_to_snake(self.name())
            self._generated_namespace = Namespace(ename, self.namespace())
        return self._generated_namespace
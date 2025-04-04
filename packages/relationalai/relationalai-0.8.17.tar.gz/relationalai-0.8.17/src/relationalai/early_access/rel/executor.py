from __future__ import annotations
import textwrap

from pandas import DataFrame
from typing import Optional
import relationalai as rai

from relationalai import debugging
from relationalai.clients import result_helpers
from relationalai.early_access.metamodel import ir, compiler, executor as e, factory as f
from relationalai.early_access.rel import Compiler

class RelExecutor(e.Executor):
    """Executes Rel code using the RAI client."""

    def __init__(self, database: str, dry_run: bool = False) -> None:
        super().__init__()
        self.database = database
        self.dry_run = dry_run
        self.compiler = Compiler()
        self._resources = None
        self._last_model = None

    @property
    def resources(self):
        if not self._resources:
            with debugging.span("create_session"):
                self._resources = rai.clients.snowflake.Resources()
                self._resources.config.set("use_graph_index", False)
                if not self.dry_run:
                    try:
                        if not self._resources.get_database(self.database):
                            self._resources.create_graph(self.database)
                    except Exception as e:
                        if "already exists" not in str(e).lower():
                            raise e
                    self.engine = self._resources.config.get("engine", strict=False)
                    if not self.engine:
                        self.engine = self._resources.get_default_engine_name()
        return self._resources

    def execute(self, model: ir.Model, task:ir.Task, observer: Optional[compiler.Observer]=None) -> DataFrame:
        resources = self.resources

        rules_code = ""
        if self._last_model != model:
            with debugging.span("compile", metamodel=model) as install_span:
                rules_code = self.compiler.compile(model, observer)
                install_span["compile_type"] = "model"
                install_span["rel"] = rules_code
                rules_code = resources.create_models_code([("pyrel_qb_0", rules_code)])
                self._last_model = model


        with debugging.span("compile", metamodel=task) as compile_span:
            task_model = f.compute_model(f.logical([task]))
            task_code = self.compiler.compile(task_model, observer, {"no_declares": True})
            compile_span["compile_type"] = "query"
            compile_span["rel"] = task_code


        full_code = textwrap.dedent(f"""
            {rules_code}
            {task_code}
        """)

        if self.dry_run:
            return DataFrame()

        raw_results = resources.exec_raw(self.database, self.engine, full_code, False, nowait_durable=True)
        df, _ = result_helpers.format_results(raw_results, None)  # Pass None for task parameter
        return df

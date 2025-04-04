import operator

from typing_extensions import TypedDict
from typing import Annotated, Literal, Optional, Dict

from nl2query.query_reframer.main import QueryReframer
from nl2query.table_selector.main import TableSelector
from nl2query.intent_engine.main import IntentEngine
from nl2query.query_builder.main import QueryBuilder
from nl2query.query_validator.main import QueryValidator
from nl2query.query_executor.main import QueryExecutor


class BaseState(TypedDict):
    state_id: int
    thread_id: str
    version: str
    response_type: Literal["streaming", "regular_run"]
    errors: Annotated[list, operator.add]
    query: str
    model_type: str
    model_name: str
    temperature: str
    results: str
    user_message: str
    raw_messages: list
    messages: list


class State(BaseState, total=False):
    tables_selector_yn: bool
    follow_up_query_yn: bool
    query_reframer_yn: bool
    query_reframer_metadata_yn: bool
    query_reframer_examples_yn: bool
    query_reframer_config_yn: bool
    query_reframer_rag_yn: bool
    refarmed_query: str
    selected_tables: list
    intent_yn: bool
    rag_yn: bool
    config_mapping: Dict
    query_builder_yn: bool
    intent_ambiguity_yn: bool
    intent_filterable_yn: bool
    query_correcter_yn: bool
    reframed_query: str
    initial_query: str
    validated_query: str
    intent_json: Dict
    intent_ambiguity: list
    regenerate_intent_yn: bool
    proceed_to_query_builder_yn: bool
    db_type: Literal["postgres", "snowflake"]
    output_response: str  # output from db
    table_selector_instance: Optional[TableSelector] = None
    query_reframer_instance: Optional[QueryReframer] = None
    intent_engine_instance: Optional[IntentEngine] = None
    query_builder_instance: Optional[QueryBuilder] = None
    query_validator_instance: Optional[QueryValidator] = None
    query_executor_instance: Optional[QueryExecutor] = None

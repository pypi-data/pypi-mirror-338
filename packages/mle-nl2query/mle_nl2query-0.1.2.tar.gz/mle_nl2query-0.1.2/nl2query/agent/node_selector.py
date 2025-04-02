from nl2query.agent.state import State
from nl2query.core.decorators import wrap_state_transition


@wrap_state_transition
def select_next_node_after_tables_selector(state: State):
    """Select next node after tables selector."""
    return "query_reframer_node" if state["query_reframer_yn"] else "intent_engine_node"


@wrap_state_transition
def select_next_node_after_query_reframer(state: State):
    """Select next node after query reframer."""
    return "intent_engine_node" if state["intent_yn"] else "query_builder_node"


@wrap_state_transition
def select_next_node_after_intent_engine(state: State):
    """Select next node after intent engine."""
    if state.get("proceed_to_query_builder_yn"):
        return "query_builder_node"
    # if state["intent_ambiguity_yn"] and state.get("intent_ambiguity", {}).get("exists"):
    if state["intent_ambiguity_yn"]:
        return "intent_ambiguity_handler_node"
    if state["intent_filterable_yn"]:
        return "intent_filter_checker_node"
    return "query_builder_node"


@wrap_state_transition
def select_next_node_after_intent_ambiguity_handler(state: State):
    """Select next node after intent ambiguity handler."""
    if state["intent_filterable_yn"]:
        return "intent_filter_checker_node"
    return "query_builder_node"


@wrap_state_transition
def select_next_node_after_intent_filter_checker(state: State):
    """Select next node after intent filter checker."""
    return "query_builder_node"


@wrap_state_transition
def select_next_node_after_query_builder(state: State):
    """Select next node after query builder."""
    return "query_corrector_node"


@wrap_state_transition
def select_next_node_after_query_corrector(state: State):
    """Select next node after query corrector."""
    return "query_executor_node"

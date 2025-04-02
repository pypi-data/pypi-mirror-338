
import os
import json

from nl2query.agent.graph import State
from nl2query.core.base_module import BaseModule


#TODO move this to path setup
file_path = __file__

work_dir = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
data_dir = os.path.join(work_dir,"data")
input_dir = os.path.join(data_dir,"input")

class IntentAmbiguityHandler(BaseModule):
    """
    A class to handle ambiguity in intent fields.
    The run() method processes ambiguity (if any) and, if the user has provided input,
    it handles that input to update how the query is reframed.
    """

    def __init__(self, system_prompt: str = None, examples: str = None,
                 ambiguous_fields_file: str = None, *args, **kwargs):
        super().__init__(system_prompt, examples, *args, **kwargs)
        if ambiguous_fields_file is None:
            #TODO remoe static path
            ambiguous_fields_file = "/Users/mac/ML-experts/ML Experts/mle_nl2query/data/input/ambigious_fields.json"
        with open(ambiguous_fields_file, "r") as f:
            self.ambiguous_data = json.load(f)

    def process_ambiguity(self, state: dict) -> dict:
        """
        Checks if the intent in state contains any ambiguous fields.
        If found, marks them as unresolved, picks the first for processing,
        and generates a clarification message which is set in state["user_message"].
        Otherwise, it marks ambiguity as not existing.
        """
        ambiguous_data_mapping = self.ambiguous_data.get("mapping", {})
        try:
            intent = state.get("intent_json", "{}")
            if isinstance(intent, dict):
                entities = intent.get("entities", [])
            else:
                entities = json.loads(intent).get("entities", [])
        except Exception:
            entities = []

        ambiguous_found = False
        ambiguous_fields = {}
        for entity in entities:
            for field in entity.get("fields", []):
                if field in ambiguous_data_mapping:
                    ambiguous_found = True
                    mapped_field = ambiguous_data_mapping[field]
                    ambiguous_fields[mapped_field] = "unresolved"
        if ambiguous_found:
            intent_ambiguity_data = {
                "exists": True,
                "ambiguous_fields": ambiguous_fields,
                "is_processing": list(ambiguous_fields.keys())[0]
            }
            user_message = self.generate_ambiguity_message(intent_ambiguity_data["is_processing"])
            state["user_message"] = user_message
            state["intent_ambiguity"] = intent_ambiguity_data
        else:
            state["intent_ambiguity"] = {"exists": False}
            # Optionally, if no ambiguity exists, we can jump directly to query building.
            if not state.get("intent_filter_yn", False):
                state["proceed_to_query_builder_yn"] = True
        return state

    def generate_ambiguity_message(self, field: str) -> str:
        """
        Generates a clarification message by listing all possible options
        for the given ambiguity category from the ambiguous_fields.json.
        """
        messages = ["Did you mean:"]
        for desc in self.ambiguous_data.get("mapping_description", {}).get(field, []):
            messages.append(f"{desc.get('idx')}. {desc.get('value')}")
        return "\n".join(messages)

    def handle_ambiguity(self, state: dict) -> dict:
        """
        Processes the user’s response (stored in state["query"]) for disambiguation.
        It updates the state's reframed query with clarification details and marks the ambiguous field as resolved.
        If additional ambiguous fields remain unresolved, it updates state["user_message"] accordingly.
        """
        user_input = state.get("query", "").strip().lower()
        ambiguous_data_description = self.ambiguous_data.get("mapping_description", {})
        intent_ambiguity_data = state.get("intent_ambiguity", {})
        processing_field = intent_ambiguity_data.get("is_processing")

        # List available option indices for the current ambiguous field.
        available_options = [str(desc.get("idx")) for desc in ambiguous_data_description.get(processing_field, [])]

        if user_input in available_options:
            for desc in ambiguous_data_description.get(processing_field, []):
                if str(desc.get("idx")) == user_input:
                    message = f"\nWe are interpreting the field as `{desc.get('field')}` ({desc.get('info')}).\n"
                    state["reframed_query"] = state.get("reframed_query", "") + message
                    state["regenerate_intent_yn"] = True

        # Mark the current ambiguous field as resolved.
        if processing_field in intent_ambiguity_data.get("ambiguous_fields", {}):
            intent_ambiguity_data["ambiguous_fields"][processing_field] = "resolved"

        unresolved_fields = [
            field for field, status in intent_ambiguity_data.get("ambiguous_fields", {}).items() if status == "unresolved"
        ]
        if unresolved_fields:
            intent_ambiguity_data["is_processing"] = unresolved_fields[0]
            state["user_message"] = self.generate_ambiguity_message(unresolved_fields[0])
        else:
            intent_ambiguity_data["exists"] = False

        state["intent_ambiguity"] = intent_ambiguity_data
        return state

    def run(self, state: dict) -> dict:
        """
        This run() method is the single entry point to the ambiguity handler.
        It first processes any ambiguous fields in the state's intent;
        if ambiguous fields exist and a user response is provided in state["query"],
        it then calls handle_ambiguity to update the state's reframed query.
        Finally, it returns the updated state.
        """
        state = self.process_ambiguity(state)
        if state.get("intent_ambiguity", {}).get("exists") and state.get("query"):
            state = self.handle_ambiguity(state)
        return state, state["intent_ambiguity"]
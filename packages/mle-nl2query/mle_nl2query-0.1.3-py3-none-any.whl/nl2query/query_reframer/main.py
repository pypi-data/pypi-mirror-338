from loguru import logger
from langchain_core.prompts import ChatPromptTemplate

from nl2query.core.base_module import BaseModule
from nl2query.query_reframer.schema import (
    QueryReframerSchema,
    QueryReframerConfigSchema,
)
from nl2query.core.llm_models import get_llm
from nl2query.query_reframer.prompts import (
    get_reframed_query_with_config_prompt,
    get_reframed_query_with_metadata_prompt,
    get_config_mapping_prompt,
)


class QueryReframer(BaseModule):
    """Concrete implementation of BaseModule for query reframing with conditional config, metadata, and examples"""

    def __init__(
        self,
        config_mapping_prompt: str = None,
        query_reframer_with_config_prompt: str = None,
        query_reframer_with_metadata_prompt: str = None,
        pydantic_class: QueryReframerSchema = QueryReframerSchema,
        query_reframer_with_config_examples: str = None,
        config_mapping_example: str = None,
        query_reframer_with_metatdata_examples: str = None,
        config: str = None,
        metadata: str = None,
        *args,
        **kwargs,
    ):
        super().__init__(
            pydantic_class=pydantic_class,
            examples=query_reframer_with_config_examples,
            *args,
            **kwargs,
        )
        self.query = ""
        self.rephrased_query = ""
        self.pydantic_class = pydantic_class
        self.config_mapping_prompt = config_mapping_prompt
        self.query_reframer_with_config_prompt = query_reframer_with_config_prompt
        self.query_reframer_with_metadata_prompt = query_reframer_with_metadata_prompt
        self.query_reframer_with_metatdata_examples = (
            query_reframer_with_metatdata_examples
        )
        self.query_reframer_with_config_examples = query_reframer_with_config_examples
        self.config_mapping_example = config_mapping_example
        self.metadata = metadata
        self.config = config

    def run(self, state):
        """Core logic to reframe the query into an SQL query based on config, metadata, and examples"""
        self.model_type = state.get("model_type", "openai")
        self.model_name = state.get("model_name", "gpt-4-1106-preview")
        self.temperature = state.get("temperature", 0.01)

        self.query = state["query"]

        if state["query_reframer_metadata_yn"]:
            self.query_reframer_with_metadata_prompt = (
                self.query_reframer_with_metadata_prompt
            )
            self.query_reframer_with_metadata_examples = (
                self.query_reframer_with_metadata_examples
            )
        elif state["query_reframer_config_yn"]:
            self.query_reframer_with_config_prompt = (
                self.query_reframer_with_config_prompt
            )
            self.query_reframer_with_config_examples = (
                self.query_reframer_with_config_examples
            )
        else:
            self.query_reframer_examples = self.examples

        if state["query_reframer_config_yn"]:
            prompt_text = get_config_mapping_prompt(
                self.query,
                self.config,
                self.config_mapping_prompt,
                self.config_mapping_example,
            )

            prompt_template = ChatPromptTemplate.from_messages(
                [("system", prompt_text), ("human", "{query}")]
            )

            llm = get_llm(
                model_type=self.model_type,
                model_name=self.model_name,
                temperature=self.temperature,
            )
            structured_llm = llm.with_structured_output(QueryReframerConfigSchema)

            few_shot_structured_llm = prompt_template | structured_llm

            response = few_shot_structured_llm.invoke({"query": self.query})
            result = response.dict()
            mapping_output = result["mapping_output"]
            state["mapping_output"] = mapping_output
            # state["raw_messages"].append(
            #     {"role": "mapping_output", "content": mapping_output}
            # )

            logger.info(f"Mapping output: {mapping_output}")

            ###############

            prompt = get_reframed_query_with_config_prompt(
                self.query,
                mapping_output,
                self.query_reframer_with_config_prompt,
                self.query_reframer_with_config_examples,
            )
            prompt_template = ChatPromptTemplate.from_messages(
                [("system", prompt_text), ("human", "{query}")]
            )
            llm = get_llm(
                model_type=self.model_type,
                model_name=self.model_name,
                temperature=self.temperature,
            )
            structured_llm = llm.with_structured_output(self.pydantic_class)

            few_shot_structured_llm = prompt_template | structured_llm

            response = few_shot_structured_llm.invoke(self.query)
            refarmed_query = response.dict()["reframed_query"]

            logger.info(f"Reframed query with config: {refarmed_query}")
            state["reframed_query"] = refarmed_query

        if state["query_reframer_metadata_yn"]:
            query = (
                state["reframed_query"]
                if state["query_reframer_config_yn"]
                else state["query"]
            )
            prompt = get_reframed_query_with_metadata_prompt(
                query,
                self.metadata,
                self.query_reframer_with_metadata_prompt,
                self.query_reframer_with_metadata_examples,
            )

            prompt = ChatPromptTemplate.from_messages(
                [("system", prompt), ("human", "{query}")]
            )

            llm = get_llm(
                model_type=self.model_type,
                model_name=self.model_name,
                temperature=self.temperature,
            )
            structured_llm = llm.with_structured_output(
                QueryReframerSchema,
            )
            few_shot_structured_llm = prompt | structured_llm

            response = few_shot_structured_llm.invoke({"query": self.query})
            rephrased_query = response.dict()["reframed_query"]
            state["reframed_query"] = rephrased_query
            logger.info(f"Reframed query: {rephrased_query}")
            state["raw_messages"].append(
                {"role": "rephrased_query", "content": self.rephrased_query}
            )

        return state, state["reframed_query"]



 `pre-commit install` add this in instllation guidelines

plan:

1. create graph. this will be configurable. using config yaml file graph will be built accordinly.
2. define state. if no state is passed while creating graph then it will take the default state. state will be modfiable while building graph. 
3. add conditional edges. get config from yaml file
4. table selector node 
5. graph builder willl return graph and mermaid diagram (done)
6. logger setup (done)
7. linter setup (done)
8. final state id fix (done)
9. memory options would be sqlite, memory, database, etc.


# sample configurations 

# graph:
# tables_selector : bool 
# query_reframer_yn : bool 
# query_reframer_metadata_yn: bool
# query_reframer_examples_yn: bool 
# query_reframer_config_yn : bool 
# query_reframer_rag_yn : bool 
# intent_yn : bool 
# intent_ambiguity_yn : bool [TBD later]
# intent_filterable_yn : bool [TBD later]
# query_correcter_yn : bool

# A graph class needs to be created here. 
# The graph will be created using the yaml file for the configuration that will be provided. 


# memory: 
# Options would be sqlite, memory, database, etc. (TBD)

#response_type : streaming or regular_run 

# There should be a method : get_graph() that returns the graph object using the configuration provided. 
# Also create a function that returns graph mermaid diagram. 
# The graph that returns streaming response or not should be decided based on the config provided.

# There should be another method that returns the response from the graph using the input provided. (Either streaming or regular response)

# from nl2query import IntentEngine 
# from nl2query import QueryBuilder

# intent_engine = IntentEngine(examples=examples,config=config,metadata=metadata)
# query_executor = QueryBuilder(examples=examples, prompt=prompt)


# graph = NL2QueryGraph(config_file_path="config.yaml", intent_engine = intent_engine, query_executor=query_executor, ....) 


1. Implement QueryReframer, IntentEngine, QueryBuilder, class. these class will accept config, metadata, prompt, examples as required.
2. Set up default prompt for each modules. If prompt is not passed then it will use default prompt.
3. NL2QueryGraph will accept each modules object as params. 

```
from nl2query import IntentEngine 
from nl2query import QueryBuilder

intent_engine = IntentEngine(examples=examples,config=config,metadata=metadata)
query_executor = QueryBuilder(examples=examples, prompt=prompt)


graph = NL2QueryGraph(config_file_path="config.yaml", intent_engine = intent_engine, query_executor=query_executor, ....) 
```
4. prompts, configs, examples will be pass via config directly/ path for prompts will be defined in config yaml.
5. compile and run the graph as per given configs.
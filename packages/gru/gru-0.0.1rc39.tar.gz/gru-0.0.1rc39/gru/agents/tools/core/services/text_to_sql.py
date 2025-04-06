from typing import Union, Optional
from gru.agents.tools.core.code_generator.sql import SQLCodeGenerator
from gru.agents.tools.core.context_retriever.sql import SQLContextRetriever
from gru.agents.tools.core.embeddings.base import EmbeddingGenerator
from gru.agents.tools.core.code_generator.models import (
    QueryIntent,
    SQLQueryResult,
    RetrievalResult,
    CandidateValuesResult,
    IntermediateQueryRequest,
    ValueReplacedQueryRequest,
)
from gru.agents.tools.core.llm_client.base import LLMClient
from gru.agents.prompts.text_to_sql import (
    QUERY_ANALYZER_USER_PROMPT_TEMPLATE,
    QUERY_ANALYZER_SYSTEM_PROMPT,
)

from gru.agents.clients.vector_db.base import VectorDBClient


class TextToSQLService:
    def __init__(
        self,
        llm_client: LLMClient,
        embedding_generator: EmbeddingGenerator,
        vector_db_client: VectorDBClient,
    ):
        self.llm_client = llm_client
        self.context_retriever = SQLContextRetriever(
            embedding_generator, vector_db_client
        )
        self.code_generator = SQLCodeGenerator(llm_client)

    async def convert_to_sql(self, query: str) -> str:
        try:
            intent = await self._analyze_query(query)
            context = await self.context_retriever.retrieve_context(query, top_k=5)
            intermediate_query_request = (
                await self._generate_intermediate_query_request(
                    query=query, context=context, intent=intent
                )
            )
            system_prompt, user_prompt = await self._generate_prompts(
                intermediate_query_request
            )
            intermediate_sql_query_result = await self._generate_sql(
                user_prompt, system_prompt
            )
            # A better check might be to see if the placeholder pattern is present in the intermediate query.
            # Can test and update as required
            if len(intermediate_sql_query_result.placeholders) == 0:
                return intermediate_sql_query_result.sql_query
            else:
                candidate_values = (
                    await self.context_retriever.retrieve_candidate_values(
                        intermediate_sql_query_result.placeholders
                    )
                )
                value_replaced_query_request = (
                    await self._generate_value_replaced_query_request(
                        query=query,
                        intermediate_query=intermediate_sql_query_result.sql_query,
                        candidate_values=candidate_values,
                    )
                )
                system_prompt, user_prompt = await self._generate_prompts(
                    value_replaced_query_request
                )
                value_replaced_sql_query_result = await self._generate_sql(
                    user_prompt, system_prompt
                )
                return value_replaced_sql_query_result.sql_query
        except Exception as e:
            return f"Error while generating SQL query: {str(e)}"

    async def _analyze_query(self, query: str) -> QueryIntent:
        user_prompt = QUERY_ANALYZER_USER_PROMPT_TEMPLATE.format(query=query)
        response = await self.llm_client.generate(
            QUERY_ANALYZER_SYSTEM_PROMPT, user_prompt
        )

        # TODO - Response parsing logic is a placeholder - will define proper response models later.

        lines = response.split("\n")
        entities = lines[0].replace("Entities:", "").strip().strip("[]").split(",")
        domains = lines[1].replace("Domains:", "").strip().strip("[]").split(",")

        return QueryIntent(
            entities=[e.strip() for e in entities if e.strip()],
            domains=[d.strip() for d in domains if d.strip()],
        )

    async def _generate_sql(
        self, system_prompt: str, user_prompt: str
    ) -> SQLQueryResult:
        return await self.code_generator.generate_code(user_prompt, system_prompt)

    async def _generate_prompts(
        self, request: Union[IntermediateQueryRequest, ValueReplacedQueryRequest]
    ) -> tuple[str, str]:
        return await self.code_generator.generate_prompts(request)

    async def _generate_intermediate_query_request(
        self,
        query: str,
        context: Optional[RetrievalResult] = None,
        intent: Optional[QueryIntent] = None,
    ) -> IntermediateQueryRequest:
        return IntermediateQueryRequest(query=query, context=context, intent=intent)

    async def _generate_value_replaced_query_request(
        self,
        query: str,
        intermediate_query: str,
        candidate_values: CandidateValuesResult,
    ) -> ValueReplacedQueryRequest:
        return ValueReplacedQueryRequest(
            query=query,
            intermediate_query=intermediate_query,
            candidate_values=candidate_values,
        )

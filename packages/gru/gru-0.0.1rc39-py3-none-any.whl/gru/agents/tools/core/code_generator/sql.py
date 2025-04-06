import json
from typing import Tuple, Union
from gru.agents.tools.core.code_generator.base import CodeGenerator
from gru.agents.tools.core.code_generator.models import (
    SQLQueryResult,
    IntermediateQueryRequest,
    ValueReplacedQueryRequest,
)
from gru.agents.prompts.sql import (
    INTERMEDIATE_SQL_GENERATOR_USER_PROMPT_TEMPLATE,
    VALUE_REPLACED_SQL_GENERATOR_USER_PROMPT_TEMPLATE,
    SQL_GENERATOR_SYSTEM_PROMPT,
)
from gru.agents.tools.core.llm_client.base import LLMClient


class SQLCodeGenerator(CodeGenerator):
    def __init__(
        self,
        llm_client: LLMClient,
        system_prompt=None,
        intermediate_query_user_prompt_template=None,
        value_replaced_query_user_prompt_template=None,
    ):
        """
        Initializes the SQL Code Generator with optional custom prompts.

        :param llm_client: The LLM client to use for generation.
        :param system_prompt: Optional custom system prompt (default: SQL_GENERATOR_SYSTEM_PROMPT).
        :param intermediate_query_user_prompt_template: Optional custom user prompt template (default: INTERMEDIATE_SQL_GENERATOR_USER_PROMPT_TEMPLATE).
        :param value_replaced_query_user_prompt_template: Optional custom user prompt template for replacing low cardinality values in a placeholder query (default: VALUE_REPLACED_SQL_GENERATOR_USER_PROMPT_TEMPLATE)
        """
        self.llm_client = llm_client
        self.system_prompt = system_prompt or SQL_GENERATOR_SYSTEM_PROMPT
        self.intermediate_query_user_prompt_template = (
            intermediate_query_user_prompt_template
            or INTERMEDIATE_SQL_GENERATOR_USER_PROMPT_TEMPLATE
        )
        self.value_replaced_query_user_prompt_template = (
            value_replaced_query_user_prompt_template
            or VALUE_REPLACED_SQL_GENERATOR_USER_PROMPT_TEMPLATE
        )

    def _handle_value_replaced_query(self, request: ValueReplacedQueryRequest) -> str:
        """
        Generate a prompt for query with values filled in.

        :param request: The value replaced query request
        :return: User prompt string
        """
        return self.value_replaced_query_user_prompt_template.format(
            query=request.query,
            intermediate_query=request.intermediate_query,
            candidate_values=request.candidate_values.column_values
            if hasattr(request, "candidate_values")
            else "",
        )

    def _handle_intermediate_query(self, request: IntermediateQueryRequest) -> str:
        """
        Generate a prompt for intermediate query with placeholders.

        :param request: The intermediate query request
        :return: User prompt string
        """
        return self.intermediate_query_user_prompt_template.format(
            query=request.query,
            schemas=request.context.schemas if hasattr(request, "context") else "",
            examples=request.context.examples if hasattr(request, "context") else "",
            documentation=request.context.documentation
            if hasattr(request, "context")
            else "",
        )

    async def generate_prompts(
        self, request: Union[IntermediateQueryRequest, ValueReplacedQueryRequest]
    ) -> Tuple[str, str]:
        """
        Generate appropriate prompts for SQL generation based on the provided request model.

        This method determines whether to generate a prompt for an intermediate query with
        placeholders or a value replaced query based on the type of request model.

        :param request: Either IntermediateQueryRequest or ValueReplacedQueryRequest
        :return: Tuple containing (system_prompt, user_prompt)
        """
        # Currently system prompt is common for both but it can be changed in the future with specific guidelines
        # and rules for each prompt type. In that case modify the code here
        system_prompt = self.system_prompt
        user_prompt = (
            self._handle_value_replaced_query(request)
            if isinstance(request, ValueReplacedQueryRequest)
            else self._handle_intermediate_query(request)
        )
        return system_prompt, user_prompt

    async def generate_code(self, user_prompt, system_prompt) -> SQLQueryResult:

        response = await self.llm_client.generate(system_prompt, user_prompt)

        try:
            response_json = json.loads(response)
            return SQLQueryResult(**response_json)
        except json.JSONDecodeError:
            return SQLQueryResult(sql_query=response)

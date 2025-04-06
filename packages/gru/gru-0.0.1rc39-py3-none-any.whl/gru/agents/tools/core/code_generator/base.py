from abc import ABC, abstractmethod
from typing import Any, Tuple, Union
from gru.agents.tools.core.code_generator.models import (
    IntermediateQueryRequest,
    ValueReplacedQueryRequest,
)


class CodeGenerator(ABC):
    def __init__(self, llm_client):
        self.llm_client = llm_client

    @abstractmethod
    async def generate_prompts(
        self, request: Union[IntermediateQueryRequest, ValueReplacedQueryRequest]
    ) -> Tuple[str, str]:
        pass

    @abstractmethod
    async def generate_code(self, user_prompt, system_prompt) -> Any:
        pass

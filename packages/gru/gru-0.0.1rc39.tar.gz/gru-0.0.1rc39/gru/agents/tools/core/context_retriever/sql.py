from typing import List
from gru.agents.tools.core.code_generator.models import (
    RetrievalResult,
    CandidateValuesResult,
)
from gru.agents.tools.core.context_retriever.base import ContextRetriever
from gru.agents.tools.core.embeddings.base import EmbeddingGenerator
from gru.agents.memory.memory_entities.examples import ExamplesRepository
from gru.agents.memory.memory_entities.domain_knowledge import DomainKnowledgeRepository
from gru.agents.memory.memory_entities.table_metadata import TableMetadataRepository
from gru.agents.memory.memory_entities.column_metadata import ColumnMetadataRepository
from gru.agents.clients.vector_db.base import VectorDBClient


class SQLContextRetriever(ContextRetriever):
    def __init__(
        self, embedding_generator: EmbeddingGenerator, vector_db_client: VectorDBClient
    ):
        repositories = [
            ("table_metadata_repo", TableMetadataRepository),
            ("table_documentation_repo", DomainKnowledgeRepository),
            ("example_queries_repo", ExamplesRepository),
            ("column_metadata_repo", ColumnMetadataRepository),
        ]

        for attr_name, repo_class in repositories:
            repo = repo_class(vector_db_client, embedding_generator)
            repo.setup()
            setattr(self, attr_name, repo)

    async def retrieve_context(self, query: str, top_k: int = 5) -> RetrievalResult:
        tables, schemas = self.table_metadata_repo.search_tables_and_schemas(
            query, top_k
        )
        examples = self.example_queries_repo.get_examples(query, top_k)
        documentation = self.table_documentation_repo.get_documentations(query, top_k)

        return RetrievalResult(
            tables=tables,
            schemas=schemas,
            documentation=documentation,
            examples=examples,
        )

    async def retrieve_candidate_values(self, placeholder_columns: List[str]):
        values_dict = {}
        for column in placeholder_columns:
            # retrieve column and table name from placeholder
            parts = column.split(".")
            if len(parts) != 2:
                raise ValueError(
                    f"Invalid format: {column}. Expected 'table.column' format."
                )
            match_criteria = {"table_name": parts[0], "column_name": parts[1]}
            candidate_values, metadata = self.column_metadata_repo.filter_search(
                match_criteria
            )
            values_dict[column] = {
                "candidate_values": candidate_values,
                "metadata": metadata,
            }
        return CandidateValuesResult(column_values=values_dict)

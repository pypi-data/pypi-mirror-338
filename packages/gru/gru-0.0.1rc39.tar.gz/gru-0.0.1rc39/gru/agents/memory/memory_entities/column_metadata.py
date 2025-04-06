from typing import Any, Dict, List
from gru.agents.tools.core.embeddings.base import EmbeddingGenerator
from gru.agents.memory.memory_entities.base import MemoryEntityRepository
from gru.agents.clients.vector_db.base import VectorDBClient
from gru.agents.clients.vector_db.models import (
    CollectionField,
    CollectionIndex,
    CollectionModel,
    FieldDataType,
)


class ColumnMetadataRepository(MemoryEntityRepository):
    COLLECTION_NAME = "canso_column_metadata"
    VECTOR_FIELD_NAME = "embeddings"
    OUTPUT_FIELDS = ["candidate_values", "metadata"]

    def __init__(
        self, vector_db_client: VectorDBClient, embedding_generator: EmbeddingGenerator
    ):
        self.vector_db_client = vector_db_client
        self.embedding_generator = embedding_generator

    def setup(self):
        fields = [
            CollectionField(
                name="table_column_composite_key",
                is_primary=True,
                data_type=FieldDataType.VARCHAR,
                max_length=400,
            ),
            CollectionField(
                name="table_name", data_type=FieldDataType.VARCHAR, max_length=200
            ),
            CollectionField(
                name="column_name", data_type=FieldDataType.VARCHAR, max_length=200
            ),
            CollectionField(
                name="candidate_values",
                data_type=FieldDataType.ARRAY,
                max_length=2048,
                element_type=FieldDataType.VARCHAR,
                max_capacity=100,
            ),
            CollectionField(name="metadata", data_type=FieldDataType.JSON),
            CollectionField(
                name="embeddings",
                data_type=FieldDataType.FLOAT_VECTOR,
                dimension=self.embedding_generator.dimension,
            ),
        ]

        indexes = [
            CollectionIndex(
                field_name="embeddings",
                params={
                    "index_type": "IVF_FLAT",
                    "metric_type": "L2",
                    "params": {"nlist": 1024},
                },
            )
        ]

        collection = CollectionModel(
            name=self.COLLECTION_NAME,
            description="Column metadata collection",
            fields=fields,
            indexes=indexes,
        )

        self.vector_db_client.create_collection(collection)

    def filter_search(self, match_criteria: Dict[str, Any]):
        results = self.vector_db_client.query_collection(
            collection_name=self.COLLECTION_NAME,
            match_criteria=match_criteria,
            output_fields=self.OUTPUT_FIELDS,
        )
        # Since this is an exact match we are only taking the first value from the result if it exists
        if results and len(results) > 0:
            # Since this is an exact match we are only taking the first value from the result
            candidate_values = results[0].get("candidate_values", [])
            metadata = results[0].get("metadata", {})
        else:
            # Return empty strings if no results found
            candidate_values = []
            metadata = {}
        return candidate_values, metadata

    def store(self, data: Dict[str, Any]):
        self._validate_fields(data)

        data["embeddings"] = self.embedding_generator.generate(
            data["table_name"] + data["column_name"]
        )
        self.vector_db_client.insert_documents(self.COLLECTION_NAME, [data])

    def update(self, data: Dict[str, Any]):
        self._validate_fields(data)
        data["embeddings"] = self.embedding_generator.generate(
            data["table_name"] + data["column_name"]
        )
        match_criteria = {
            "table_name": data["table_name"],
            "column_name": data["column_name"],
        }

        self.vector_db_client.update_document(
            self.COLLECTION_NAME, match_criteria, data
        )

    def delete(self, match_criteria: dict[str, Any]):
        self.vector_db_client.delete_document(self.COLLECTION_NAME, match_criteria)

    def search(self, query: str, top_k: int = 5) -> List[Dict[str, Any]]:
        query_vector = self.embedding_generator.generate(query)

        results = self.vector_db_client.similarity_search(
            collection_name=self.COLLECTION_NAME,
            vector_field=self.VECTOR_FIELD_NAME,
            query_vector=query_vector,
            top_k=top_k,
            output_fields=self.OUTPUT_FIELDS,
        )

        return results

    def _validate_fields(self, data: Dict[str, Any]):
        required_fields = [
            "table_column_composite_key",
            "table_name",
            "column_name",
            "candidate_values",
            "metadata",
        ]
        for field in required_fields:
            if field not in data:
                raise Exception(f"Missing field {field} in data")

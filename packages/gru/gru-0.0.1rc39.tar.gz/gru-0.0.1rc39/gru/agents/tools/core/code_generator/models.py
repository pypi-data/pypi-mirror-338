from pydantic import BaseModel, Field
from typing import List, Dict, Optional


class QueryIntent(BaseModel):
    entities: List[str]
    domains: List[str]


class RetrievalResult(BaseModel):
    tables: List[str]
    schemas: List[str]
    documentation: List[str]
    examples: List[str]
    low_cardinality_values: List[str] = []
    domain_knowledge: List[str] = []
    opt_rules: List[str] = []


class CandidateValuesResult(BaseModel):
    column_values: Dict


class SQLQueryResult(BaseModel):
    sql_query: str
    tables_used: Optional[List[str]] = None
    columns_used: Optional[List[str]] = None
    join_conditions: Optional[List[str]] = None
    placeholders: Optional[List[str]] = None


class QueryRequestBase(BaseModel):
    query: str


class IntermediateQueryRequest(QueryRequestBase):
    context: Optional[RetrievalResult] = Field(default_factory=RetrievalResult)
    intent: Optional[QueryIntent] = Field(default_factory=QueryIntent)


class ValueReplacedQueryRequest(QueryRequestBase):
    intermediate_query: str
    candidate_values: Optional[CandidateValuesResult] = Field(
        default_factory=CandidateValuesResult
    )

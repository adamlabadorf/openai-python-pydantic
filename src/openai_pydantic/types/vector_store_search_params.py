# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from pydantic import BaseModel, Field
from typing import List, Optional

from typing import List,Optional,Union
from typing_extensions import Literal

from .shared_params.compound_filter import CompoundFilter
from .shared_params.comparison_filter import ComparisonFilter

__all__ = ["VectorStoreSearchParams", "Filters", "RankingOptions"]


class VectorStoreSearchParams(BaseModel):
    query: "Union[str, List[str]]"
    
    """A query string for a search"""

    filters: "Optional[Filters]"= None
    
    """A filter to apply based on file attributes."""

    max_num_results: "Optional[int]"= None
    
    """The maximum number of results to return.

    This number should be between 1 and 50 inclusive.
    """

    ranking_options: "Optional[RankingOptions]"= None
    
    """Ranking options for search."""

    rewrite_query: "Optional[bool]"= None
    
    """Whether to rewrite the natural language query for vector search."""


Filters = Union[ComparisonFilter, CompoundFilter]


class RankingOptions(BaseModel):
    ranker: "Optional[Literal['auto', 'default-2024-11-15']]"= None
    

    score_threshold: "Optional[float]"= None
    
VectorStoreSearchParams.model_rebuild()
RankingOptions.model_rebuild()


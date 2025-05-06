# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from pydantic import BaseModel, Field
from typing import List, Optional

from typing import Optional,Union,List
from typing_extensions import Literal

from ..shared_params.compound_filter import CompoundFilter
from ..shared_params.comparison_filter import ComparisonFilter

__all__ = ["FileSearchToolParam", "Filters", "RankingOptions"]

Filters = Union[ComparisonFilter, CompoundFilter]


class RankingOptions(BaseModel):
    ranker: "Optional[Literal['auto', 'default-2024-11-15']]"= None
    
    """The ranker to use for the file search."""

    score_threshold: "Optional[float]"= None
    
    """The score threshold for the file search, a number between 0 and 1.

    Numbers closer to 1 will attempt to return only the most relevant results, but
    may return fewer results.
    """


class FileSearchToolParam(BaseModel):
    type: "Literal['file_search']"= None
    
    """The type of the file search tool. Always `file_search`."""

    vector_store_ids: "List[str]"= None
    
    """The IDs of the vector stores to search."""

    filters: "Optional[Filters]"= None
    
    """A filter to apply."""

    max_num_results: "Optional[int]"= None
    
    """The maximum number of results to return.

    This number should be between 1 and 50 inclusive.
    """

    ranking_options: "Optional[RankingOptions]"= None
    
    """Ranking options for search."""
RankingOptions.model_rebuild()
FileSearchToolParam.model_rebuild()


# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union
from typing_extensions import Literal
from pydantic import BaseModel
from .shared_params.compound_filter import CompoundFilter
from .shared_params.comparison_filter import ComparisonFilter

__all__ = ["VectorStoreSearchParams", "Filters", "RankingOptions"]


class VectorStoreSearchParams(BaseModel):
    query: Optional[Union[str, List[str]]] = None
    # old  query: Union[str, List[str]] = None
    # old  query: Required[Union[str, List[str]]]
    """A query string for a search"""

    filters: Optional[Filters] = None
    # old  filters: Optional[Filters] = None
    # old  filters: Filters
    """A filter to apply based on file attributes."""

    max_num_results: Optional[int] = None
    # old  max_num_results: Optional[int] = None
    # old  max_num_results: int
    """The maximum number of results to return.

    This number should be between 1 and 50 inclusive.
    """

    ranking_options: Optional[RankingOptions] = None
    # old  ranking_options: Optional[RankingOptions] = None
    # old  ranking_options: RankingOptions
    """Ranking options for search."""

    rewrite_query: Optional[bool] = None
    # old  rewrite_query: Optional[bool] = None
    # old  rewrite_query: bool
    """Whether to rewrite the natural language query for vector search."""


Filters = Union[ComparisonFilter, CompoundFilter] # old Filters: TypeAlias = Union[ComparisonFilter, CompoundFilter]


class RankingOptions(BaseModel):
    ranker: Optional[Literal["auto", "default-2024-11-15"]] = None
    # old  ranker: Optional[Literal["auto", "default-2024-11-15"]] = None
    # old  ranker: Literal["auto", "default-2024-11-15"]

    score_threshold: Optional[float] = None
    # old  score_threshold: Optional[float] = None
    # old  score_threshold: float



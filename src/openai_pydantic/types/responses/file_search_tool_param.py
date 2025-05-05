# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union, Optional
from typing_extensions import Literal
from pydantic import BaseModel
from ..shared_params.compound_filter import CompoundFilter
from ..shared_params.comparison_filter import ComparisonFilter

__all__ = ["FileSearchToolParam", "Filters", "RankingOptions"]

Filters = Union[ComparisonFilter, CompoundFilter] # old Filters: TypeAlias = Union[ComparisonFilter, CompoundFilter]


class RankingOptions(BaseModel):
    ranker: Optional[Literal["auto", "default-2024-11-15"]] = None
    # old  ranker: Optional[Literal["auto", "default-2024-11-15"]] = None
    # old  ranker: Literal["auto", "default-2024-11-15"]
    """The ranker to use for the file search."""

    score_threshold: Optional[float] = None
    # old  score_threshold: Optional[float] = None
    # old  score_threshold: float
    """The score threshold for the file search, a number between 0 and 1.

    Numbers closer to 1 will attempt to return only the most relevant results, but
    may return fewer results.
    """


class FileSearchToolParam(BaseModel):
    type: Optional[Literal["file_search"]] = None
    # old  type: Literal["file_search"] = None
    # old  type: Required[Literal["file_search"]]
    """The type of the file search tool. Always `file_search`."""

    vector_store_ids: Optional[List[str]] = None
    # old  vector_store_ids: List[str] = None
    # old  vector_store_ids: Required[List[str]]
    """The IDs of the vector stores to search."""

    filters: Optional[Filters] = None
    # old  filters: Optional[Filters] = None
    # old  filters: Optional[Filters]
    """A filter to apply."""

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



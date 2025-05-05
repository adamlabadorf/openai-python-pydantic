# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable
from typing_extensions import Literal
from pydantic import BaseModel
from .comparison_filter import ComparisonFilter

__all__ = ["CompoundFilter", "Filter"]

Filter = Union[ComparisonFilter, object] # old Filter: TypeAlias = Union[ComparisonFilter, object]


class CompoundFilter(BaseModel):
    filters: List[Filter] = None
    # old  filters: Required[Iterable[Filter]]
    """Array of filters to combine.

    Items can be `ComparisonFilter` or `CompoundFilter`.
    """

    type: Literal["and", "or"] = None
    # old  type: Required[Literal["and", "or"]]
    """Type of operation: `and` or `or`."""


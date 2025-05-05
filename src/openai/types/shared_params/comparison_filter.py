# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from typing_extensions import Literal
from pydantic import BaseModel
__all__ = ["ComparisonFilter"]


class ComparisonFilter(BaseModel):
    key: str = None
    # old  key: Required[str]
    """The key to compare against the value."""

    type: Literal["eq", "ne", "gt", "gte", "lt", "lte"] = None
    # old  type: Required[Literal["eq", "ne", "gt", "gte", "lt", "lte"]]
    """Specifies the comparison operator: `eq`, `ne`, `gt`, `gte`, `lt`, `lte`.

    - `eq`: equals
    - `ne`: not equal
    - `gt`: greater than
    - `gte`: greater than or equal
    - `lt`: less than
    - `lte`: less than or equal
    """

    value: Union[str, float, bool] = None
    # old  value: Required[Union[str, float, bool]]
    """
    The value to compare against the attribute key; supports string, number, or
    boolean types.
    """


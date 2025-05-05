# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal
from pydantic import BaseModel
__all__ = ["OutputItemListParams"]


class OutputItemListParams(BaseModel):
    eval_id: str = None
    # old  eval_id: Required[str]

    after: Optional[str] = None
    # old  after: str
    """Identifier for the last output item from the previous pagination request."""

    limit: Optional[int] = None
    # old  limit: int
    """Number of output items to retrieve."""

    order: Optional[Literal["asc", "desc"]] = None
    # old  order: Literal["asc", "desc"]
    """Sort order for output items by timestamp.

    Use `asc` for ascending order or `desc` for descending order. Defaults to `asc`.
    """

    status: Optional[Literal["fail", "pass"]] = None
    # old  status: Literal["fail", "pass"]
    """Filter output items by status.

    Use `failed` to filter by failed output items or `pass` to filter by passed
    output items.
    """


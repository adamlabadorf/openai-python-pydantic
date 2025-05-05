# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal
from pydantic import BaseModel
__all__ = ["RunListParams"]


class RunListParams(BaseModel):
    after: Optional[str] = None
    # old  after: str
    """Identifier for the last run from the previous pagination request."""

    limit: Optional[int] = None
    # old  limit: int
    """Number of runs to retrieve."""

    order: Optional[Literal["asc", "desc"]] = None
    # old  order: Literal["asc", "desc"]
    """Sort order for runs by timestamp.

    Use `asc` for ascending order or `desc` for descending order. Defaults to `asc`.
    """

    status: Optional[Literal["queued", "in_progress", "completed", "canceled", "failed"]] = None
    # old  status: Literal["queued", "in_progress", "completed", "canceled", "failed"]
    """Filter runs by status.

    One of `queued` | `in_progress` | `failed` | `completed` | `canceled`.
    """


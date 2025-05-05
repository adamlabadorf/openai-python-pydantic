# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal
from pydantic import BaseModel
__all__ = ["EvalListParams"]


class EvalListParams(BaseModel):
    after: Optional[str] = None
    # old  after: str
    """Identifier for the last eval from the previous pagination request."""

    limit: Optional[int] = None
    # old  limit: int
    """Number of evals to retrieve."""

    order: Optional[Literal["asc", "desc"]] = None
    # old  order: Literal["asc", "desc"]
    """Sort order for evals by timestamp.

    Use `asc` for ascending order or `desc` for descending order.
    """

    order_by: Optional[Literal["created_at", "updated_at"]] = None
    # old  order_by: Literal["created_at", "updated_at"]
    """Evals can be ordered by creation time or last updated time.

    Use `created_at` for creation time or `updated_at` for last updated time.
    """


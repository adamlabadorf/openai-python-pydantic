# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from pydantic import BaseModel, Field
from typing import List, Optional

from typing_extensions import Literal

__all__ = ["RunListParams"]


class RunListParams(BaseModel):
    after: "Optional[str]"= None
    
    """Identifier for the last run from the previous pagination request."""

    limit: "Optional[int]"= None
    
    """Number of runs to retrieve."""

    order: "Optional[Literal['asc', 'desc']]"= None
    
    """Sort order for runs by timestamp.

    Use `asc` for ascending order or `desc` for descending order. Defaults to `asc`.
    """

    status: "Optional[Literal['queued', 'in_progress', 'completed', 'canceled', 'failed']]"= None
    
    """Filter runs by status.

    One of `queued` | `in_progress` | `failed` | `completed` | `canceled`.
    """
RunListParams.model_rebuild()


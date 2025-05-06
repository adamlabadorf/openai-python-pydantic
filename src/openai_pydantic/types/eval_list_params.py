# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from pydantic import BaseModel, Field
from typing import List, Optional

from typing_extensions import Literal

__all__ = ["EvalListParams"]


class EvalListParams(BaseModel):
    after: "Optional[str]"= None
    
    """Identifier for the last eval from the previous pagination request."""

    limit: "Optional[int]"= None
    
    """Number of evals to retrieve."""

    order: "Optional[Literal['asc', 'desc']]"= None
    
    """Sort order for evals by timestamp.

    Use `asc` for ascending order or `desc` for descending order.
    """

    order_by: "Optional[Literal['created_at', 'updated_at']]"= None
    
    """Evals can be ordered by creation time or last updated time.

    Use `created_at` for creation time or `updated_at` for last updated time.
    """
EvalListParams.model_rebuild()


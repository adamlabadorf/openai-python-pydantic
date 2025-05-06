# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from pydantic import BaseModel, Field
from typing import List, Optional

from typing_extensions import Literal

__all__ = ["OutputItemListParams"]


class OutputItemListParams(BaseModel):
    eval_id: "str"= None
    

    after: "Optional[str]"= None
    
    """Identifier for the last output item from the previous pagination request."""

    limit: "Optional[int]"= None
    
    """Number of output items to retrieve."""

    order: "Optional[Literal['asc', 'desc']]"= None
    
    """Sort order for output items by timestamp.

    Use `asc` for ascending order or `desc` for descending order. Defaults to `asc`.
    """

    status: "Optional[Literal['fail', 'pass']]"= None
    
    """Filter output items by status.

    Use `failed` to filter by failed output items or `pass` to filter by passed
    output items.
    """
OutputItemListParams.model_rebuild()


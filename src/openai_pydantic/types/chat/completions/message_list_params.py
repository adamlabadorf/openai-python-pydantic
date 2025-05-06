# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from pydantic import BaseModel, Field
from typing import List, Optional

from typing_extensions import Literal

__all__ = ["MessageListParams"]


class MessageListParams(BaseModel):
    after: "Optional[str]"= None
    
    """Identifier for the last message from the previous pagination request."""

    limit: "Optional[int]"= None
    
    """Number of messages to retrieve."""

    order: "Optional[Literal['asc', 'desc']]"= None
    
    """Sort order for messages by timestamp.

    Use `asc` for ascending order or `desc` for descending order. Defaults to `asc`.
    """
MessageListParams.model_rebuild()


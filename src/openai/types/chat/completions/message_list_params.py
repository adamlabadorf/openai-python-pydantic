# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal
from pydantic import BaseModel
__all__ = ["MessageListParams"]


class MessageListParams(BaseModel):
    after: Optional[str] = None
    # old  after: str
    """Identifier for the last message from the previous pagination request."""

    limit: Optional[int] = None
    # old  limit: int
    """Number of messages to retrieve."""

    order: Optional[Literal["asc", "desc"]] = None
    # old  order: Literal["asc", "desc"]
    """Sort order for messages by timestamp.

    Use `asc` for ascending order or `desc` for descending order. Defaults to `asc`.
    """


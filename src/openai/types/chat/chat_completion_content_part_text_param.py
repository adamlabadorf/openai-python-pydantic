# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal
from pydantic import BaseModel
__all__ = ["ChatCompletionContentPartTextParam"]


class ChatCompletionContentPartTextParam(BaseModel):
    text: str = None
    # old  text: Required[str]
    """The text content."""

    type: Literal["text"] = None
    # old  type: Required[Literal["text"]]
    """The type of the content part."""


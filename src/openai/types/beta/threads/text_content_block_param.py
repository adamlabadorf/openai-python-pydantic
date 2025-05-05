# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal
from pydantic import BaseModel
__all__ = ["TextContentBlockParam"]


class TextContentBlockParam(BaseModel):
    text: str = None
    # old  text: Required[str]
    """Text content to be sent to the model"""

    type: Literal["text"] = None
    # old  type: Required[Literal["text"]]
    """Always `text`."""


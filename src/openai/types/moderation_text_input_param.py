# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal
from pydantic import BaseModel
__all__ = ["ModerationTextInputParam"]


class ModerationTextInputParam(BaseModel):
    text: str = None
    # old  text: Required[str]
    """A string of text to classify."""

    type: Literal["text"] = None
    # old  type: Required[Literal["text"]]
    """Always `text`."""


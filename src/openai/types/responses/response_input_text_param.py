# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal
from pydantic import BaseModel
__all__ = ["ResponseInputTextParam"]


class ResponseInputTextParam(BaseModel):
    text: str = None
    # old  text: Required[str]
    """The text input to the model."""

    type: Literal["input_text"] = None
    # old  type: Required[Literal["input_text"]]
    """The type of the input item. Always `input_text`."""


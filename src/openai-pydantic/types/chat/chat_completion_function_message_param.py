# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal
from pydantic import BaseModel
__all__ = ["ChatCompletionFunctionMessageParam"]


class ChatCompletionFunctionMessageParam(BaseModel):
    content: Optional[str] = None
    # old  content: Required[Optional[str]]
    """The contents of the function message."""

    name: str = None
    # old  name: Required[str]
    """The name of the function to call."""

    role: Literal["function"] = None
    # old  role: Required[Literal["function"]]
    """The role of the messages author, in this case `function`."""


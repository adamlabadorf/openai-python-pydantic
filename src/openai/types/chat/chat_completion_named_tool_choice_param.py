# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal
from pydantic import BaseModel
__all__ = ["ChatCompletionNamedToolChoiceParam", "Function"]


class Function(BaseModel):
    name: Optional[str] = None
    # old  name: str = None
    # old  name: Required[str]
    """The name of the function to call."""


class ChatCompletionNamedToolChoiceParam(BaseModel):
    function: Optional[Function] = None
    # old  function: Function = None
    # old  function: Required[Function]

    type: Optional[Literal["function"]] = None
    # old  type: Literal["function"] = None
    # old  type: Required[Literal["function"]]
    """The type of the tool. Currently, only `function` is supported."""



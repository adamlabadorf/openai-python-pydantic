# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal
from pydantic import BaseModel
from ..shared_params.function_definition import FunctionDefinition

__all__ = ["ChatCompletionToolParam"]


class ChatCompletionToolParam(BaseModel):
    function: FunctionDefinition = None
    # old  function: Required[FunctionDefinition]

    type: Literal["function"] = None
    # old  type: Required[Literal["function"]]
    """The type of the tool. Currently, only `function` is supported."""


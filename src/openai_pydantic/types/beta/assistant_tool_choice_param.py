# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal
from pydantic import BaseModel
from .assistant_tool_choice_function_param import AssistantToolChoiceFunctionParam

__all__ = ["AssistantToolChoiceParam"]


class AssistantToolChoiceParam(BaseModel):
    type: Literal["function", "code_interpreter", "file_search"] = None
    # old  type: Required[Literal["function", "code_interpreter", "file_search"]]
    """The type of the tool. If type is `function`, the function name must be set"""

    function: Optional[AssistantToolChoiceFunctionParam] = None
    # old  function: AssistantToolChoiceFunctionParam


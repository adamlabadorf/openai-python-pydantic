# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from pydantic import BaseModel, Field
from typing import List, Optional

from typing_extensions import Literal

__all__ = ["ChatCompletionNamedToolChoiceParam", "Function"]


class Function(BaseModel):
    name: "str"
    
    """The name of the function to call."""


class ChatCompletionNamedToolChoiceParam(BaseModel):
    function: "Function"
    

    type: "Literal['function']"
    
    """The type of the tool. Currently, only `function` is supported."""
Function.model_rebuild()
ChatCompletionNamedToolChoiceParam.model_rebuild()


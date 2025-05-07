# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from pydantic import BaseModel, Field
from typing import List, Optional

from typing_extensions import Literal

__all__ = ["ToolChoiceFunctionParam"]


class ToolChoiceFunctionParam(BaseModel):
    name: "str"
    
    """The name of the function to call."""

    type: "Literal['function']"
    
    """For function calling, the type is always `function`."""
ToolChoiceFunctionParam.model_rebuild()


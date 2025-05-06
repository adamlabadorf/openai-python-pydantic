# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from pydantic import BaseModel, Field
from typing import List, Optional


__all__ = ["AssistantToolChoiceFunctionParam"]


class AssistantToolChoiceFunctionParam(BaseModel):
    name: "str"= None
    
    """The name of the function to call."""
AssistantToolChoiceFunctionParam.model_rebuild()


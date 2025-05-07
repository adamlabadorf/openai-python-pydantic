# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from pydantic import BaseModel, Field
from typing import List, Optional


__all__ = ["ChatCompletionFunctionCallOptionParam"]


class ChatCompletionFunctionCallOptionParam(BaseModel):
    name: "str"
    
    """The name of the function to call."""
ChatCompletionFunctionCallOptionParam.model_rebuild()


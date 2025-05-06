# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from pydantic import BaseModel, Field
from typing import List, Optional

from typing import Optional
from typing_extensions import Literal

__all__ = ["ChatCompletionFunctionMessageParam"]


class ChatCompletionFunctionMessageParam(BaseModel):
    content: "Optional[str]"= None
    
    """The contents of the function message."""

    name: "str"= None
    
    """The name of the function to call."""

    role: "Literal['function']"= None
    
    """The role of the messages author, in this case `function`."""
ChatCompletionFunctionMessageParam.model_rebuild()


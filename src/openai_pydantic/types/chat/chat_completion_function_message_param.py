# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from pydantic import BaseModel, Field
from typing import List, Optional

from typing import Optional
from typing_extensions import Literal

__all__ = ["ChatCompletionFunctionMessageParam"]


class ChatCompletionFunctionMessageParam(BaseModel):
    content: "Optional[str]"
    
    """The contents of the function message."""

    name: "str"
    
    """The name of the function to call."""

    role: "Literal['function']"
    
    """The role of the messages author, in this case `function`."""
ChatCompletionFunctionMessageParam.model_rebuild()


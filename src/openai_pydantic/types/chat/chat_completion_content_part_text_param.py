# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from pydantic import BaseModel, Field
from typing import List, Optional

from typing_extensions import Literal

__all__ = ["ChatCompletionContentPartTextParam"]


class ChatCompletionContentPartTextParam(BaseModel):
    text: "str"
    
    """The text content."""

    type: "Literal['text']"
    
    """The type of the content part."""
ChatCompletionContentPartTextParam.model_rebuild()


# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from pydantic import BaseModel, Field
from typing import List, Optional

from typing_extensions import Literal

__all__ = ["TextContentBlockParam"]


class TextContentBlockParam(BaseModel):
    text: "str"
    
    """Text content to be sent to the model"""

    type: "Literal['text']"
    
    """Always `text`."""
TextContentBlockParam.model_rebuild()


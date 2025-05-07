# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from pydantic import BaseModel, Field
from typing import List, Optional

from typing_extensions import Literal

__all__ = ["ModerationTextInputParam"]


class ModerationTextInputParam(BaseModel):
    text: "str"
    
    """A string of text to classify."""

    type: "Literal['text']"
    
    """Always `text`."""
ModerationTextInputParam.model_rebuild()


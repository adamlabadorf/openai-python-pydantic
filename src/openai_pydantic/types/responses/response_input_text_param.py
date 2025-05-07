# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from pydantic import BaseModel, Field
from typing import List, Optional

from typing_extensions import Literal

__all__ = ["ResponseInputTextParam"]


class ResponseInputTextParam(BaseModel):
    text: "str"
    
    """The text input to the model."""

    type: "Literal['input_text']"
    
    """The type of the input item. Always `input_text`."""
ResponseInputTextParam.model_rebuild()


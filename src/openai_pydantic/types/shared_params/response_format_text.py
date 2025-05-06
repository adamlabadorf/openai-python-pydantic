# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from pydantic import BaseModel, Field
from typing import List, Optional

from typing_extensions import Literal

__all__ = ["ResponseFormatText"]


class ResponseFormatText(BaseModel):
    type: "Literal['text']"= None
    
    """The type of response format being defined. Always `text`."""
ResponseFormatText.model_rebuild()


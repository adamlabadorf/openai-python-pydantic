# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from pydantic import BaseModel, Field
from typing import List, Optional

from typing_extensions import Literal

__all__ = ["ResponseFormatJSONObject"]


class ResponseFormatJSONObject(BaseModel):
    type: "Literal['json_object']"
    
    """The type of response format being defined. Always `json_object`."""
ResponseFormatJSONObject.model_rebuild()


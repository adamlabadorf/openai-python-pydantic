# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal
from pydantic import BaseModel
__all__ = ["ResponseFormatJSONObject"]


class ResponseFormatJSONObject(BaseModel):
    type: Literal["json_object"] = None
    # old  type: Required[Literal["json_object"]]
    """The type of response format being defined. Always `json_object`."""


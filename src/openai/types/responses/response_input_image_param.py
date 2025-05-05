# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal
from pydantic import BaseModel
__all__ = ["ResponseInputImageParam"]


class ResponseInputImageParam(BaseModel):
    detail: Literal["low", "high", "auto"] = None
    # old  detail: Required[Literal["low", "high", "auto"]]
    """The detail level of the image to be sent to the model.

    One of `high`, `low`, or `auto`. Defaults to `auto`.
    """

    type: Literal["input_image"] = None
    # old  type: Required[Literal["input_image"]]
    """The type of the input item. Always `input_image`."""

    file_id: Optional[str] = None
    # old  file_id: Optional[str]
    """The ID of the file to be sent to the model."""

    image_url: Optional[str] = None
    # old  image_url: Optional[str]
    """The URL of the image to be sent to the model.

    A fully qualified URL or base64 encoded image in a data URL.
    """


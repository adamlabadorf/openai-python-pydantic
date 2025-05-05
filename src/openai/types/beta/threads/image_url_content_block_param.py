# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal
from pydantic import BaseModel
from .image_url_param import ImageURLParam

__all__ = ["ImageURLContentBlockParam"]


class ImageURLContentBlockParam(BaseModel):
    image_url: ImageURLParam = None
    # old  image_url: Required[ImageURLParam]

    type: Literal["image_url"] = None
    # old  type: Required[Literal["image_url"]]
    """The type of the content part."""


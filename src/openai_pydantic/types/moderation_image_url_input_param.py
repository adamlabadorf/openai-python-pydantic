# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal
from pydantic import BaseModel
__all__ = ["ModerationImageURLInputParam", "ImageURL"]


class ImageURL(BaseModel):
    url: Optional[str] = None
    # old  url: str = None
    # old  url: Required[str]
    """Either a URL of the image or the base64 encoded image data."""


class ModerationImageURLInputParam(BaseModel):
    image_url: Optional[ImageURL] = None
    # old  image_url: ImageURL = None
    # old  image_url: Required[ImageURL]
    """Contains either an image URL or a data URL for a base64 encoded image."""

    type: Optional[Literal["image_url"]] = None
    # old  type: Literal["image_url"] = None
    # old  type: Required[Literal["image_url"]]
    """Always `image_url`."""



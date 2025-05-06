# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from pydantic import BaseModel, Field
from typing import List, Optional

from typing_extensions import Literal

__all__ = ["ModerationImageURLInputParam", "ImageURL"]


class ImageURL(BaseModel):
    url: "str"= None
    
    """Either a URL of the image or the base64 encoded image data."""


class ModerationImageURLInputParam(BaseModel):
    image_url: "ImageURL"= None
    
    """Contains either an image URL or a data URL for a base64 encoded image."""

    type: "Literal['image_url']"= None
    
    """Always `image_url`."""
ImageURL.model_rebuild()
ModerationImageURLInputParam.model_rebuild()


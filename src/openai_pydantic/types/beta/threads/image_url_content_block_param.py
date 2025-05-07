# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from pydantic import BaseModel, Field
from typing import List, Optional

from typing_extensions import Literal

from .image_url_param import ImageURLParam

__all__ = ["ImageURLContentBlockParam"]


class ImageURLContentBlockParam(BaseModel):
    image_url: "ImageURLParam"
    

    type: "Literal['image_url']"
    
    """The type of the content part."""
ImageURLContentBlockParam.model_rebuild()


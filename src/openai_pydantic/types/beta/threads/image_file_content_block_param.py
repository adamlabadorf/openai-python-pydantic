# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from pydantic import BaseModel, Field
from typing import List, Optional

from typing_extensions import Literal

from .image_file_param import ImageFileParam

__all__ = ["ImageFileContentBlockParam"]


class ImageFileContentBlockParam(BaseModel):
    image_file: "ImageFileParam"
    

    type: "Literal['image_file']"
    
    """Always `image_file`."""
ImageFileContentBlockParam.model_rebuild()


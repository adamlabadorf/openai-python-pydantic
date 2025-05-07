# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from pydantic import BaseModel, Field
from typing import List, Optional

from typing_extensions import Literal

__all__ = ["ImageURLParam"]


class ImageURLParam(BaseModel):
    url: "str"
    
    """
    The external URL of the image, must be a supported image types: jpeg, jpg, png,
    gif, webp.
    """

    detail: "Optional[Literal['auto', 'low', 'high']]"= None
    
    """Specifies the detail level of the image.

    `low` uses fewer tokens, you can opt in to high resolution using `high`. Default
    value is `auto`
    """
ImageURLParam.model_rebuild()


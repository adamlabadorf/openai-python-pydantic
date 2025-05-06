# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from pydantic import BaseModel, Field
from typing import List, Optional

from typing_extensions import Literal

__all__ = ["ChatCompletionContentPartImageParam", "ImageURL"]


class ImageURL(BaseModel):
    url: "str"= None
    
    """Either a URL of the image or the base64 encoded image data."""

    detail: "Optional[Literal['auto', 'low', 'high']]"= None
    
    """Specifies the detail level of the image.

    Learn more in the
    [Vision guide](https://platform.openai.com/docs/guides/vision#low-or-high-fidelity-image-understanding).
    """


class ChatCompletionContentPartImageParam(BaseModel):
    image_url: "ImageURL"= None
    

    type: "Literal['image_url']"= None
    
    """The type of the content part."""
ImageURL.model_rebuild()
ChatCompletionContentPartImageParam.model_rebuild()


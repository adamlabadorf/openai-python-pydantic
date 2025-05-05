# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal
from pydantic import BaseModel
__all__ = ["ChatCompletionContentPartImageParam", "ImageURL"]


class ImageURL(BaseModel):
    url: Optional[str] = None
    # old  url: str = None
    # old  url: Required[str]
    """Either a URL of the image or the base64 encoded image data."""

    detail: Optional[Literal["auto", "low", "high"]] = None
    # old  detail: Optional[Literal["auto", "low", "high"]] = None
    # old  detail: Literal["auto", "low", "high"]
    """Specifies the detail level of the image.

    Learn more in the
    [Vision guide](https://platform.openai.com/docs/guides/vision#low-or-high-fidelity-image-understanding).
    """


class ChatCompletionContentPartImageParam(BaseModel):
    image_url: Optional[ImageURL] = None
    # old  image_url: ImageURL = None
    # old  image_url: Required[ImageURL]

    type: Optional[Literal["image_url"]] = None
    # old  type: Literal["image_url"] = None
    # old  type: Required[Literal["image_url"]]
    """The type of the content part."""



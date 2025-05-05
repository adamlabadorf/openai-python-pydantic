# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal
from pydantic import BaseModel
__all__ = ["ImageURLParam"]


class ImageURLParam(BaseModel):
    url: str = None
    # old  url: Required[str]
    """
    The external URL of the image, must be a supported image types: jpeg, jpg, png,
    gif, webp.
    """

    detail: Optional[Literal["auto", "low", "high"]] = None
    # old  detail: Literal["auto", "low", "high"]
    """Specifies the detail level of the image.

    `low` uses fewer tokens, you can opt in to high resolution using `high`. Default
    value is `auto`
    """


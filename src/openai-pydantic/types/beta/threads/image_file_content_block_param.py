# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal
from pydantic import BaseModel
from .image_file_param import ImageFileParam

__all__ = ["ImageFileContentBlockParam"]


class ImageFileContentBlockParam(BaseModel):
    image_file: ImageFileParam = None
    # old  image_file: Required[ImageFileParam]

    type: Literal["image_file"] = None
    # old  type: Required[Literal["image_file"]]
    """Always `image_file`."""


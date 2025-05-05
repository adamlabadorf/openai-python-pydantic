# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from pydantic import BaseModel
from ..._types import FileTypes

__all__ = ["PartCreateParams"]


class PartCreateParams(BaseModel):
    data: FileTypes = None
    # old  data: Required[FileTypes]
    """The chunk of bytes for this Part."""


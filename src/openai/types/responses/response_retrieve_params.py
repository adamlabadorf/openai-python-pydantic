# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from pydantic import BaseModel
from .response_includable import ResponseIncludable

__all__ = ["ResponseRetrieveParams"]


class ResponseRetrieveParams(BaseModel):
    include: Optional[List[ResponseIncludable]] = None
    # old  include: List[ResponseIncludable]
    """Additional fields to include in the response.

    See the `include` parameter for Response creation above for more information.
    """


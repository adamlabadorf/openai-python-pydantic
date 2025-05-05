# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal
from pydantic import BaseModel
__all__ = ["ResponseOutputRefusalParam"]


class ResponseOutputRefusalParam(BaseModel):
    refusal: str = None
    # old  refusal: Required[str]
    """The refusal explanationfrom the model."""

    type: Literal["refusal"] = None
    # old  type: Required[Literal["refusal"]]
    """The type of the refusal. Always `refusal`."""


# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from pydantic import BaseModel
__all__ = ["AssistantToolChoiceFunctionParam"]


class AssistantToolChoiceFunctionParam(BaseModel):
    name: str = None
    # old  name: Required[str]
    """The name of the function to call."""


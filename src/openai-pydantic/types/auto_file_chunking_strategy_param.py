# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal
from pydantic import BaseModel
__all__ = ["AutoFileChunkingStrategyParam"]


class AutoFileChunkingStrategyParam(BaseModel):
    type: Literal["auto"] = None
    # old  type: Required[Literal["auto"]]
    """Always `auto`."""


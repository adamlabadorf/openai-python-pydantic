# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal
from pydantic import BaseModel
from .static_file_chunking_strategy_param import StaticFileChunkingStrategyParam

__all__ = ["StaticFileChunkingStrategyObjectParam"]


class StaticFileChunkingStrategyObjectParam(BaseModel):
    static: StaticFileChunkingStrategyParam = None
    # old  static: Required[StaticFileChunkingStrategyParam]

    type: Literal["static"] = None
    # old  type: Required[Literal["static"]]
    """Always `static`."""


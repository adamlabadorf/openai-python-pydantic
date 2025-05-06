# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from pydantic import BaseModel, Field
from typing import List, Optional

from typing_extensions import Literal

from .static_file_chunking_strategy_param import StaticFileChunkingStrategyParam

__all__ = ["StaticFileChunkingStrategyObjectParam"]


class StaticFileChunkingStrategyObjectParam(BaseModel):
    static: "StaticFileChunkingStrategyParam"= None
    

    type: "Literal['static']"= None
    
    """Always `static`."""
StaticFileChunkingStrategyObjectParam.model_rebuild()


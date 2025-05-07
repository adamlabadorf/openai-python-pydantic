# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from pydantic import BaseModel, Field
from typing import List, Optional

from typing_extensions import Literal

__all__ = ["AutoFileChunkingStrategyParam"]


class AutoFileChunkingStrategyParam(BaseModel):
    type: "Literal['auto']"
    
    """Always `auto`."""
AutoFileChunkingStrategyParam.model_rebuild()


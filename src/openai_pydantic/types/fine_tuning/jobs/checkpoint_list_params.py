# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from pydantic import BaseModel, Field
from typing import List, Optional


__all__ = ["CheckpointListParams"]


class CheckpointListParams(BaseModel):
    after: "Optional[str]"= None
    
    """Identifier for the last checkpoint ID from the previous pagination request."""

    limit: "Optional[int]"= None
    
    """Number of checkpoints to retrieve."""
CheckpointListParams.model_rebuild()


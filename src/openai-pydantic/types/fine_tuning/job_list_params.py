# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Optional
from pydantic import BaseModel
__all__ = ["JobListParams"]


class JobListParams(BaseModel):
    after: Optional[str] = None
    # old  after: str
    """Identifier for the last job from the previous pagination request."""

    limit: Optional[int] = None
    # old  limit: int
    """Number of fine-tuning jobs to retrieve."""

    metadata: Optional[Dict[str, str]] = None
    # old  metadata: Optional[Dict[str, str]]
    """Optional metadata filter.

    To filter, use the syntax `metadata[k]=v`. Alternatively, set `metadata=null` to
    indicate no metadata.
    """


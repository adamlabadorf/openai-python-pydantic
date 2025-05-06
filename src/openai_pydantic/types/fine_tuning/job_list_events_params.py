# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from pydantic import BaseModel, Field
from typing import List, Optional


__all__ = ["JobListEventsParams"]


class JobListEventsParams(BaseModel):
    after: "Optional[str]"= None
    
    """Identifier for the last event from the previous pagination request."""

    limit: "Optional[int]"= None
    
    """Number of events to retrieve."""
JobListEventsParams.model_rebuild()


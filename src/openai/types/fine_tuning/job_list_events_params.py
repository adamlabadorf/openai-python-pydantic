# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from pydantic import BaseModel
__all__ = ["JobListEventsParams"]


class JobListEventsParams(BaseModel):
    after: Optional[str] = None
    # old  after: str
    """Identifier for the last event from the previous pagination request."""

    limit: Optional[int] = None
    # old  limit: int
    """Number of events to retrieve."""


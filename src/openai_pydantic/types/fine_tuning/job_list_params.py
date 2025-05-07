# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from pydantic import BaseModel, Field
from typing import List, Optional

from typing import Optional,Dict

__all__ = ["JobListParams"]


class JobListParams(BaseModel):
    after: "Optional[str]"= None
    
    """Identifier for the last job from the previous pagination request."""

    limit: "Optional[int]"= None
    
    """Number of fine-tuning jobs to retrieve."""

    metadata: "Optional[Dict[str, str]]"= None
    
    """Optional metadata filter.

    To filter, use the syntax `metadata[k]=v`. Alternatively, set `metadata=null` to
    indicate no metadata.
    """
JobListParams.model_rebuild()


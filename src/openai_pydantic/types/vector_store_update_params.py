# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from pydantic import BaseModel, Field
from typing import List, Optional

from typing import Optional
from typing_extensions import Literal

from .shared_params.metadata import Metadata

__all__ = ["VectorStoreUpdateParams", "ExpiresAfter"]


class VectorStoreUpdateParams(BaseModel):
    expires_after: "Optional[ExpiresAfter]"= None
    
    """The expiration policy for a vector store."""

    metadata: "Optional[Metadata]"= None
    
    """Set of 16 key-value pairs that can be attached to an object.

    This can be useful for storing additional information about the object in a
    structured format, and querying for objects via API or the dashboard.

    Keys are strings with a maximum length of 64 characters. Values are strings with
    a maximum length of 512 characters.
    """

    name: "Optional[str]"= None
    
    """The name of the vector store."""


class ExpiresAfter(BaseModel):
    anchor: "Literal['last_active_at']"
    
    """Anchor timestamp after which the expiration policy applies.

    Supported anchors: `last_active_at`.
    """

    days: "int"
    
    """The number of days after the anchor time that the vector store will expire."""
VectorStoreUpdateParams.model_rebuild()
ExpiresAfter.model_rebuild()


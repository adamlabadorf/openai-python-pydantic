# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from pydantic import BaseModel, Field
from typing import List, Optional

from typing_extensions import Literal

__all__ = ["PermissionRetrieveParams"]


class PermissionRetrieveParams(BaseModel):
    after: "Optional[str]"= None
    
    """Identifier for the last permission ID from the previous pagination request."""

    limit: "Optional[int]"= None
    
    """Number of permissions to retrieve."""

    order: "Optional[Literal['ascending', 'descending']]"= None
    
    """The order in which to retrieve permissions."""

    project_id: "Optional[str]"= None
    
    """The ID of the project to get permissions for."""
PermissionRetrieveParams.model_rebuild()


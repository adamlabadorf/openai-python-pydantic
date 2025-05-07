# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from pydantic import BaseModel, Field
from typing import List, Optional

from typing import List,Optional

__all__ = ["PermissionCreateParams"]


class PermissionCreateParams(BaseModel):
    project_ids: "List[str]"
    
    """The project identifiers to grant access to."""
PermissionCreateParams.model_rebuild()


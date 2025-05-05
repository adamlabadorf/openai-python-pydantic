# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal
from pydantic import BaseModel
__all__ = ["PermissionRetrieveParams"]


class PermissionRetrieveParams(BaseModel):
    after: Optional[str] = None
    # old  after: str
    """Identifier for the last permission ID from the previous pagination request."""

    limit: Optional[int] = None
    # old  limit: int
    """Number of permissions to retrieve."""

    order: Optional[Literal["ascending", "descending"]] = None
    # old  order: Literal["ascending", "descending"]
    """The order in which to retrieve permissions."""

    project_id: Optional[str] = None
    # old  project_id: str
    """The ID of the project to get permissions for."""


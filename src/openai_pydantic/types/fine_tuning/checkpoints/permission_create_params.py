# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from pydantic import BaseModel
__all__ = ["PermissionCreateParams"]


class PermissionCreateParams(BaseModel):
    project_ids: List[str] = None
    # old  project_ids: Required[List[str]]
    """The project identifiers to grant access to."""


# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal
from pydantic import BaseModel
__all__ = ["ComputerToolParam"]


class ComputerToolParam(BaseModel):
    display_height: int = None
    # old  display_height: Required[int]
    """The height of the computer display."""

    display_width: int = None
    # old  display_width: Required[int]
    """The width of the computer display."""

    environment: Literal["windows", "mac", "linux", "ubuntu", "browser"] = None
    # old  environment: Required[Literal["windows", "mac", "linux", "ubuntu", "browser"]]
    """The type of computer environment to control."""

    type: Literal["computer_use_preview"] = None
    # old  type: Required[Literal["computer_use_preview"]]
    """The type of the computer use tool. Always `computer_use_preview`."""


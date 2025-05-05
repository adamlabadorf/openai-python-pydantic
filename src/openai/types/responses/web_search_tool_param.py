# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal
from pydantic import BaseModel
__all__ = ["WebSearchToolParam", "UserLocation"]


class UserLocation(BaseModel):
    type: Optional[Literal["approximate"]] = None
    # old  type: Literal["approximate"] = None
    # old  type: Required[Literal["approximate"]]
    """The type of location approximation. Always `approximate`."""

    city: Optional[str] = None
    # old  city: Optional[str] = None
    # old  city: Optional[str]
    """Free text input for the city of the user, e.g. `San Francisco`."""

    country: Optional[str] = None
    # old  country: Optional[str] = None
    # old  country: Optional[str]
    """
    The two-letter [ISO country code](https://en.wikipedia.org/wiki/ISO_3166-1) of
    the user, e.g. `US`.
    """

    region: Optional[str] = None
    # old  region: Optional[str] = None
    # old  region: Optional[str]
    """Free text input for the region of the user, e.g. `California`."""

    timezone: Optional[str] = None
    # old  timezone: Optional[str] = None
    # old  timezone: Optional[str]
    """
    The [IANA timezone](https://timeapi.io/documentation/iana-timezones) of the
    user, e.g. `America/Los_Angeles`.
    """


class WebSearchToolParam(BaseModel):
    type: Optional[Literal["web_search_preview", "web_search_preview_2025_03_11"]] = None
    # old  type: Literal["web_search_preview", "web_search_preview_2025_03_11"] = None
    # old  type: Required[Literal["web_search_preview", "web_search_preview_2025_03_11"]]
    """The type of the web search tool.

    One of `web_search_preview` or `web_search_preview_2025_03_11`.
    """

    search_context_size: Optional[Literal["low", "medium", "high"]] = None
    # old  search_context_size: Optional[Literal["low", "medium", "high"]] = None
    # old  search_context_size: Literal["low", "medium", "high"]
    """High level guidance for the amount of context window space to use for the
    search.

    One of `low`, `medium`, or `high`. `medium` is the default.
    """

    user_location: Optional[UserLocation] = None
    # old  user_location: Optional[UserLocation] = None
    # old  user_location: Optional[UserLocation]
    """The user's location."""



# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from pydantic import BaseModel, Field
from typing import List, Optional

from typing import Optional
from typing_extensions import Literal

__all__ = ["WebSearchToolParam", "UserLocation"]


class UserLocation(BaseModel):
    type: "Literal['approximate']"= None
    
    """The type of location approximation. Always `approximate`."""

    city: "Optional[str]"= None
    
    """Free text input for the city of the user, e.g. `San Francisco`."""

    country: "Optional[str]"= None
    
    """
    The two-letter [ISO country code](https://en.wikipedia.org/wiki/ISO_3166-1) of
    the user, e.g. `US`.
    """

    region: "Optional[str]"= None
    
    """Free text input for the region of the user, e.g. `California`."""

    timezone: "Optional[str]"= None
    
    """
    The [IANA timezone](https://timeapi.io/documentation/iana-timezones) of the
    user, e.g. `America/Los_Angeles`.
    """


class WebSearchToolParam(BaseModel):
    type: "Literal['web_search_preview', 'web_search_preview_2025_03_11']"= None
    
    """The type of the web search tool.

    One of `web_search_preview` or `web_search_preview_2025_03_11`.
    """

    search_context_size: "Optional[Literal['low', 'medium', 'high']]"= None
    
    """High level guidance for the amount of context window space to use for the
    search.

    One of `low`, `medium`, or `high`. `medium` is the default.
    """

    user_location: "Optional[UserLocation]"= None
    
    """The user's location."""
UserLocation.model_rebuild()
WebSearchToolParam.model_rebuild()


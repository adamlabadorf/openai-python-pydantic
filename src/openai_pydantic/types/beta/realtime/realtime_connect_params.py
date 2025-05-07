# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from pydantic import BaseModel, Field
from typing import List, Optional


__all__ = ["RealtimeConnectParams"]


class RealtimeConnectParams(BaseModel):
    model: "str"
    
RealtimeConnectParams.model_rebuild()


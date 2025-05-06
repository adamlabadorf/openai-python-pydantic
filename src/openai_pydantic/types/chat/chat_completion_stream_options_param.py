# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from pydantic import BaseModel, Field
from typing import List, Optional


__all__ = ["ChatCompletionStreamOptionsParam"]


class ChatCompletionStreamOptionsParam(BaseModel):
    include_usage: "Optional[bool]"= None
    
    """If set, an additional chunk will be streamed before the `data: [DONE]` message.

    The `usage` field on this chunk shows the token usage statistics for the entire
    request, and the `choices` field will always be an empty array.

    All other chunks will also include a `usage` field, but with a null value.
    **NOTE:** If the stream is interrupted, you may not receive the final usage
    chunk which contains the total token usage for the request.
    """
ChatCompletionStreamOptionsParam.model_rebuild()


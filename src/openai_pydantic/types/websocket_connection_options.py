# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from pydantic import BaseModel, ConfigDict
from typing import Optional
from typing_extensions import Sequence

from websockets import Subprotocol
from websockets.extensions import ClientExtensionFactory


class WebsocketConnectionOptions(BaseModel):
    """Websocket connection options copied from `websockets`.

    For example: https://websockets.readthedocs.io/en/stable/reference/asyncio/client.html#websockets.asyncio.client.connect
    """

    model_config = ConfigDict(arbitrary_types_allowed=True)

    extensions: "Optional[Sequence[ClientExtensionFactory]]"= None
    
    """List of supported extensions, in order in which they should be negotiated and run."""

    subprotocols: "Optional[Sequence[Subprotocol]]"= None
    
    """List of supported subprotocols, in order of decreasing preference."""

    compression: "Optional[str]"= None
    
    """The “permessage-deflate” extension is enabled by default. Set compression to None to disable it. See the [compression guide](https://websockets.readthedocs.io/en/stable/topics/compression.html) for details."""

    # limits
    max_size: "Optional[int]"= None
    
    """Maximum size of incoming messages in bytes. None disables the limit."""

    max_queue: "Optional[int | tuple[int | None, int | None]]"= None
    
    """High-water mark of the buffer where frames are received. It defaults to 16 frames. The low-water mark defaults to max_queue // 4. You may pass a (high, low) tuple to set the high-water and low-water marks. If you want to disable flow control entirely, you may set it to None, although that’s a bad idea."""

    write_limit: "Optional[int | tuple[int, int | None]]"= None
    
    """High-water mark of write buffer in bytes. It is passed to set_write_buffer_limits(). It defaults to 32 KiB. You may pass a (high, low) tuple to set the high-water and low-water marks."""
WebsocketConnectionOptions.model_rebuild()


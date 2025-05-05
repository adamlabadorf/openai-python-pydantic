# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union, Iterable, Optional
from typing_extensions import Literal
from pydantic import BaseModel
from ..shared_params.metadata import Metadata
from .code_interpreter_tool_param import CodeInterpreterToolParam
from .threads.message_content_part_param import MessageContentPartParam

__all__ = [
    "ThreadCreateParams",
    "Message",
    "MessageAttachment",
    "MessageAttachmentTool",
    "MessageAttachmentToolFileSearch",
    "ToolResources",
    "ToolResourcesCodeInterpreter",
    "ToolResourcesFileSearch",
    "ToolResourcesFileSearchVectorStore",
    "ToolResourcesFileSearchVectorStoreChunkingStrategy",
    "ToolResourcesFileSearchVectorStoreChunkingStrategyAuto",
    "ToolResourcesFileSearchVectorStoreChunkingStrategyStatic",
    "ToolResourcesFileSearchVectorStoreChunkingStrategyStaticStatic",
]


class ThreadCreateParams(BaseModel):
    messages: Optional[List[Message]] = None
    # old  messages: Optional[List[Message]] = None
    # old  messages: Optional[List[Message]] = None
    # old  messages: Optional[List[Message]] = None
    # old  messages: Optional[List[Message]] = None
    # old  messages: Optional[List[Message]] = None
    # old  messages: Optional[List[Message]] = None
    # old  messages: Optional[List[Message]] = None
    # old  messages: Optional[List[Message]] = None
    # old  messages: Optional[List[Message]] = None
    # old  messages: Optional[List[Message]] = None
    # old  messages: Iterable[Message]
    """
    A list of [messages](https://platform.openai.com/docs/api-reference/messages) to
    start the thread with.
    """

    metadata: Optional[Metadata] = None
    # old  metadata: Optional[Metadata] = None
    # old  metadata: Optional[Metadata] = None
    # old  metadata: Optional[Metadata] = None
    # old  metadata: Optional[Metadata] = None
    # old  metadata: Optional[Metadata] = None
    # old  metadata: Optional[Metadata] = None
    # old  metadata: Optional[Metadata] = None
    # old  metadata: Optional[Metadata] = None
    # old  metadata: Optional[Metadata] = None
    # old  metadata: Optional[Metadata] = None
    # old  metadata: Optional[Metadata]
    """Set of 16 key-value pairs that can be attached to an object.

    This can be useful for storing additional information about the object in a
    structured format, and querying for objects via API or the dashboard.

    Keys are strings with a maximum length of 64 characters. Values are strings with
    a maximum length of 512 characters.
    """

    tool_resources: Optional[ToolResources] = None
    # old  tool_resources: Optional[ToolResources] = None
    # old  tool_resources: Optional[ToolResources] = None
    # old  tool_resources: Optional[ToolResources] = None
    # old  tool_resources: Optional[ToolResources] = None
    # old  tool_resources: Optional[ToolResources] = None
    # old  tool_resources: Optional[ToolResources] = None
    # old  tool_resources: Optional[ToolResources] = None
    # old  tool_resources: Optional[ToolResources] = None
    # old  tool_resources: Optional[ToolResources] = None
    # old  tool_resources: Optional[ToolResources] = None
    # old  tool_resources: Optional[ToolResources]
    """
    A set of resources that are made available to the assistant's tools in this
    thread. The resources are specific to the type of tool. For example, the
    `code_interpreter` tool requires a list of file IDs, while the `file_search`
    tool requires a list of vector store IDs.
    """


class MessageAttachmentToolFileSearch(BaseModel):
    type: Optional[Literal["file_search"]] = None
    # old  type: Optional[Literal["file_search"]] = None
    # old  type: Optional[Literal["file_search"]] = None
    # old  type: Optional[Literal["file_search"]] = None
    # old  type: Optional[Literal["file_search"]] = None
    # old  type: Optional[Literal["file_search"]] = None
    # old  type: Optional[Literal["file_search"]] = None
    # old  type: Optional[Literal["file_search"]] = None
    # old  type: Optional[Literal["file_search"]] = None
    # old  type: Optional[Literal["file_search"]] = None
    # old  type: Literal["file_search"] = None
    # old  type: Required[Literal["file_search"]]
    """The type of tool being defined: `file_search`"""


MessageAttachmentTool = Union[CodeInterpreterToolParam, MessageAttachmentToolFileSearch] # old MessageAttachmentTool: TypeAlias = Union[CodeInterpreterToolParam, MessageAttachmentToolFileSearch]


class MessageAttachment(BaseModel):
    file_id: Optional[str] = None
    # old  file_id: Optional[str] = None
    # old  file_id: Optional[str] = None
    # old  file_id: Optional[str] = None
    # old  file_id: Optional[str] = None
    # old  file_id: Optional[str] = None
    # old  file_id: Optional[str] = None
    # old  file_id: Optional[str] = None
    # old  file_id: Optional[str] = None
    # old  file_id: Optional[str] = None
    # old  file_id: Optional[str] = None
    # old  file_id: str
    """The ID of the file to attach to the message."""

    tools: Optional[List[MessageAttachmentTool]] = None
    # old  tools: Optional[List[MessageAttachmentTool]] = None
    # old  tools: Optional[List[MessageAttachmentTool]] = None
    # old  tools: Optional[List[MessageAttachmentTool]] = None
    # old  tools: Optional[List[MessageAttachmentTool]] = None
    # old  tools: Optional[List[MessageAttachmentTool]] = None
    # old  tools: Optional[List[MessageAttachmentTool]] = None
    # old  tools: Optional[List[MessageAttachmentTool]] = None
    # old  tools: Optional[List[MessageAttachmentTool]] = None
    # old  tools: Optional[List[MessageAttachmentTool]] = None
    # old  tools: Optional[List[MessageAttachmentTool]] = None
    # old  tools: Iterable[MessageAttachmentTool]
    """The tools to add this file to."""


class Message(BaseModel):
    content: Optional[Union[str, List[MessageContentPartParam]]] = None
    # old  content: Optional[Union[str, List[MessageContentPartParam]]] = None
    # old  content: Optional[Union[str, List[MessageContentPartParam]]] = None
    # old  content: Optional[Union[str, List[MessageContentPartParam]]] = None
    # old  content: Optional[Union[str, List[MessageContentPartParam]]] = None
    # old  content: Optional[Union[str, List[MessageContentPartParam]]] = None
    # old  content: Optional[Union[str, List[MessageContentPartParam]]] = None
    # old  content: Optional[Union[str, List[MessageContentPartParam]]] = None
    # old  content: Optional[Union[str, List[MessageContentPartParam]]] = None
    # old  content: Optional[Union[str, List[MessageContentPartParam]]] = None
    # old  content: Union[str, List[MessageContentPartParam]] = None
    # old  content: Required[Union[str, Iterable[MessageContentPartParam]]]
    """The text contents of the message."""

    role: Optional[Literal["user", "assistant"]] = None
    # old  role: Optional[Literal["user", "assistant"]] = None
    # old  role: Optional[Literal["user", "assistant"]] = None
    # old  role: Optional[Literal["user", "assistant"]] = None
    # old  role: Optional[Literal["user", "assistant"]] = None
    # old  role: Optional[Literal["user", "assistant"]] = None
    # old  role: Optional[Literal["user", "assistant"]] = None
    # old  role: Optional[Literal["user", "assistant"]] = None
    # old  role: Optional[Literal["user", "assistant"]] = None
    # old  role: Optional[Literal["user", "assistant"]] = None
    # old  role: Literal["user", "assistant"] = None
    # old  role: Required[Literal["user", "assistant"]]
    """The role of the entity that is creating the message. Allowed values include:

    - `user`: Indicates the message is sent by an actual user and should be used in
      most cases to represent user-generated messages.
    - `assistant`: Indicates the message is generated by the assistant. Use this
      value to insert messages from the assistant into the conversation.
    """

    attachments: Optional[List[MessageAttachment]] = None
    # old  attachments: Optional[List[MessageAttachment]] = None
    # old  attachments: Optional[List[MessageAttachment]] = None
    # old  attachments: Optional[List[MessageAttachment]] = None
    # old  attachments: Optional[List[MessageAttachment]] = None
    # old  attachments: Optional[List[MessageAttachment]] = None
    # old  attachments: Optional[List[MessageAttachment]] = None
    # old  attachments: Optional[List[MessageAttachment]] = None
    # old  attachments: Optional[List[MessageAttachment]] = None
    # old  attachments: Optional[List[MessageAttachment]] = None
    # old  attachments: Optional[List[MessageAttachment]] = None
    # old  attachments: Optional[Iterable[MessageAttachment]]
    """A list of files attached to the message, and the tools they should be added to."""

    metadata: Optional[Metadata] = None
    # old  metadata: Optional[Metadata] = None
    # old  metadata: Optional[Metadata] = None
    # old  metadata: Optional[Metadata] = None
    # old  metadata: Optional[Metadata] = None
    # old  metadata: Optional[Metadata] = None
    # old  metadata: Optional[Metadata] = None
    # old  metadata: Optional[Metadata] = None
    # old  metadata: Optional[Metadata] = None
    # old  metadata: Optional[Metadata] = None
    # old  metadata: Optional[Metadata] = None
    # old  metadata: Optional[Metadata]
    """Set of 16 key-value pairs that can be attached to an object.

    This can be useful for storing additional information about the object in a
    structured format, and querying for objects via API or the dashboard.

    Keys are strings with a maximum length of 64 characters. Values are strings with
    a maximum length of 512 characters.
    """


class ToolResourcesCodeInterpreter(BaseModel):
    file_ids: Optional[List[str]] = None
    # old  file_ids: Optional[List[str]] = None
    # old  file_ids: Optional[List[str]] = None
    # old  file_ids: Optional[List[str]] = None
    # old  file_ids: Optional[List[str]] = None
    # old  file_ids: Optional[List[str]] = None
    # old  file_ids: Optional[List[str]] = None
    # old  file_ids: Optional[List[str]] = None
    # old  file_ids: Optional[List[str]] = None
    # old  file_ids: Optional[List[str]] = None
    # old  file_ids: Optional[List[str]] = None
    # old  file_ids: List[str]
    """
    A list of [file](https://platform.openai.com/docs/api-reference/files) IDs made
    available to the `code_interpreter` tool. There can be a maximum of 20 files
    associated with the tool.
    """


class ToolResourcesFileSearchVectorStoreChunkingStrategyAuto(BaseModel):
    type: Optional[Literal["auto"]] = None
    # old  type: Optional[Literal["auto"]] = None
    # old  type: Optional[Literal["auto"]] = None
    # old  type: Optional[Literal["auto"]] = None
    # old  type: Optional[Literal["auto"]] = None
    # old  type: Optional[Literal["auto"]] = None
    # old  type: Optional[Literal["auto"]] = None
    # old  type: Optional[Literal["auto"]] = None
    # old  type: Optional[Literal["auto"]] = None
    # old  type: Optional[Literal["auto"]] = None
    # old  type: Literal["auto"] = None
    # old  type: Required[Literal["auto"]]
    """Always `auto`."""


class ToolResourcesFileSearchVectorStoreChunkingStrategyStaticStatic(BaseModel):
    chunk_overlap_tokens: Optional[int] = None
    # old  chunk_overlap_tokens: Optional[int] = None
    # old  chunk_overlap_tokens: Optional[int] = None
    # old  chunk_overlap_tokens: Optional[int] = None
    # old  chunk_overlap_tokens: Optional[int] = None
    # old  chunk_overlap_tokens: Optional[int] = None
    # old  chunk_overlap_tokens: Optional[int] = None
    # old  chunk_overlap_tokens: Optional[int] = None
    # old  chunk_overlap_tokens: Optional[int] = None
    # old  chunk_overlap_tokens: Optional[int] = None
    # old  chunk_overlap_tokens: int = None
    # old  chunk_overlap_tokens: Required[int]
    """The number of tokens that overlap between chunks. The default value is `400`.

    Note that the overlap must not exceed half of `max_chunk_size_tokens`.
    """

    max_chunk_size_tokens: Optional[int] = None
    # old  max_chunk_size_tokens: Optional[int] = None
    # old  max_chunk_size_tokens: Optional[int] = None
    # old  max_chunk_size_tokens: Optional[int] = None
    # old  max_chunk_size_tokens: Optional[int] = None
    # old  max_chunk_size_tokens: Optional[int] = None
    # old  max_chunk_size_tokens: Optional[int] = None
    # old  max_chunk_size_tokens: Optional[int] = None
    # old  max_chunk_size_tokens: Optional[int] = None
    # old  max_chunk_size_tokens: Optional[int] = None
    # old  max_chunk_size_tokens: int = None
    # old  max_chunk_size_tokens: Required[int]
    """The maximum number of tokens in each chunk.

    The default value is `800`. The minimum value is `100` and the maximum value is
    `4096`.
    """


class ToolResourcesFileSearchVectorStoreChunkingStrategyStatic(BaseModel):
    static: Optional[ToolResourcesFileSearchVectorStoreChunkingStrategyStaticStatic] = None
    # old  static: Optional[ToolResourcesFileSearchVectorStoreChunkingStrategyStaticStatic] = None
    # old  static: Optional[ToolResourcesFileSearchVectorStoreChunkingStrategyStaticStatic] = None
    # old  static: Optional[ToolResourcesFileSearchVectorStoreChunkingStrategyStaticStatic] = None
    # old  static: Optional[ToolResourcesFileSearchVectorStoreChunkingStrategyStaticStatic] = None
    # old  static: Optional[ToolResourcesFileSearchVectorStoreChunkingStrategyStaticStatic] = None
    # old  static: Optional[ToolResourcesFileSearchVectorStoreChunkingStrategyStaticStatic] = None
    # old  static: Optional[ToolResourcesFileSearchVectorStoreChunkingStrategyStaticStatic] = None
    # old  static: Optional[ToolResourcesFileSearchVectorStoreChunkingStrategyStaticStatic] = None
    # old  static: Optional[ToolResourcesFileSearchVectorStoreChunkingStrategyStaticStatic] = None
    # old  static: ToolResourcesFileSearchVectorStoreChunkingStrategyStaticStatic = None
    # old  static: Required[ToolResourcesFileSearchVectorStoreChunkingStrategyStaticStatic]

    type: Optional[Literal["static"]] = None
    # old  type: Optional[Literal["static"]] = None
    # old  type: Optional[Literal["static"]] = None
    # old  type: Optional[Literal["static"]] = None
    # old  type: Optional[Literal["static"]] = None
    # old  type: Optional[Literal["static"]] = None
    # old  type: Optional[Literal["static"]] = None
    # old  type: Optional[Literal["static"]] = None
    # old  type: Optional[Literal["static"]] = None
    # old  type: Optional[Literal["static"]] = None
    # old  type: Literal["static"] = None
    # old  type: Required[Literal["static"]]
    """Always `static`."""


ToolResourcesFileSearchVectorStoreChunkingStrategy = Union[ # old ToolResourcesFileSearchVectorStoreChunkingStrategy: TypeAlias = Union[
    ToolResourcesFileSearchVectorStoreChunkingStrategyAuto, ToolResourcesFileSearchVectorStoreChunkingStrategyStatic
]


class ToolResourcesFileSearchVectorStore(BaseModel):
    chunking_strategy: Optional[ToolResourcesFileSearchVectorStoreChunkingStrategy] = None
    # old  chunking_strategy: Optional[ToolResourcesFileSearchVectorStoreChunkingStrategy] = None
    # old  chunking_strategy: Optional[ToolResourcesFileSearchVectorStoreChunkingStrategy] = None
    # old  chunking_strategy: Optional[ToolResourcesFileSearchVectorStoreChunkingStrategy] = None
    # old  chunking_strategy: Optional[ToolResourcesFileSearchVectorStoreChunkingStrategy] = None
    # old  chunking_strategy: Optional[ToolResourcesFileSearchVectorStoreChunkingStrategy] = None
    # old  chunking_strategy: Optional[ToolResourcesFileSearchVectorStoreChunkingStrategy] = None
    # old  chunking_strategy: Optional[ToolResourcesFileSearchVectorStoreChunkingStrategy] = None
    # old  chunking_strategy: Optional[ToolResourcesFileSearchVectorStoreChunkingStrategy] = None
    # old  chunking_strategy: Optional[ToolResourcesFileSearchVectorStoreChunkingStrategy] = None
    # old  chunking_strategy: Optional[ToolResourcesFileSearchVectorStoreChunkingStrategy] = None
    # old  chunking_strategy: ToolResourcesFileSearchVectorStoreChunkingStrategy
    """The chunking strategy used to chunk the file(s).

    If not set, will use the `auto` strategy.
    """

    file_ids: Optional[List[str]] = None
    # old  file_ids: Optional[List[str]] = None
    # old  file_ids: Optional[List[str]] = None
    # old  file_ids: Optional[List[str]] = None
    # old  file_ids: Optional[List[str]] = None
    # old  file_ids: Optional[List[str]] = None
    # old  file_ids: Optional[List[str]] = None
    # old  file_ids: Optional[List[str]] = None
    # old  file_ids: Optional[List[str]] = None
    # old  file_ids: Optional[List[str]] = None
    # old  file_ids: Optional[List[str]] = None
    # old  file_ids: List[str]
    """
    A list of [file](https://platform.openai.com/docs/api-reference/files) IDs to
    add to the vector store. There can be a maximum of 10000 files in a vector
    store.
    """

    metadata: Optional[Metadata] = None
    # old  metadata: Optional[Metadata] = None
    # old  metadata: Optional[Metadata] = None
    # old  metadata: Optional[Metadata] = None
    # old  metadata: Optional[Metadata] = None
    # old  metadata: Optional[Metadata] = None
    # old  metadata: Optional[Metadata] = None
    # old  metadata: Optional[Metadata] = None
    # old  metadata: Optional[Metadata] = None
    # old  metadata: Optional[Metadata] = None
    # old  metadata: Optional[Metadata] = None
    # old  metadata: Optional[Metadata]
    """Set of 16 key-value pairs that can be attached to an object.

    This can be useful for storing additional information about the object in a
    structured format, and querying for objects via API or the dashboard.

    Keys are strings with a maximum length of 64 characters. Values are strings with
    a maximum length of 512 characters.
    """


class ToolResourcesFileSearch(BaseModel):
    vector_store_ids: Optional[List[str]] = None
    # old  vector_store_ids: Optional[List[str]] = None
    # old  vector_store_ids: Optional[List[str]] = None
    # old  vector_store_ids: Optional[List[str]] = None
    # old  vector_store_ids: Optional[List[str]] = None
    # old  vector_store_ids: Optional[List[str]] = None
    # old  vector_store_ids: Optional[List[str]] = None
    # old  vector_store_ids: Optional[List[str]] = None
    # old  vector_store_ids: Optional[List[str]] = None
    # old  vector_store_ids: Optional[List[str]] = None
    # old  vector_store_ids: Optional[List[str]] = None
    # old  vector_store_ids: List[str]
    """
    The
    [vector store](https://platform.openai.com/docs/api-reference/vector-stores/object)
    attached to this thread. There can be a maximum of 1 vector store attached to
    the thread.
    """

    vector_stores: Optional[List[ToolResourcesFileSearchVectorStore]] = None
    # old  vector_stores: Optional[List[ToolResourcesFileSearchVectorStore]] = None
    # old  vector_stores: Optional[List[ToolResourcesFileSearchVectorStore]] = None
    # old  vector_stores: Optional[List[ToolResourcesFileSearchVectorStore]] = None
    # old  vector_stores: Optional[List[ToolResourcesFileSearchVectorStore]] = None
    # old  vector_stores: Optional[List[ToolResourcesFileSearchVectorStore]] = None
    # old  vector_stores: Optional[List[ToolResourcesFileSearchVectorStore]] = None
    # old  vector_stores: Optional[List[ToolResourcesFileSearchVectorStore]] = None
    # old  vector_stores: Optional[List[ToolResourcesFileSearchVectorStore]] = None
    # old  vector_stores: Optional[List[ToolResourcesFileSearchVectorStore]] = None
    # old  vector_stores: Optional[List[ToolResourcesFileSearchVectorStore]] = None
    # old  vector_stores: Iterable[ToolResourcesFileSearchVectorStore]
    """
    A helper to create a
    [vector store](https://platform.openai.com/docs/api-reference/vector-stores/object)
    with file_ids and attach it to this thread. There can be a maximum of 1 vector
    store attached to the thread.
    """


class ToolResources(BaseModel):
    code_interpreter: Optional[ToolResourcesCodeInterpreter] = None
    # old  code_interpreter: Optional[ToolResourcesCodeInterpreter] = None
    # old  code_interpreter: Optional[ToolResourcesCodeInterpreter] = None
    # old  code_interpreter: Optional[ToolResourcesCodeInterpreter] = None
    # old  code_interpreter: Optional[ToolResourcesCodeInterpreter] = None
    # old  code_interpreter: Optional[ToolResourcesCodeInterpreter] = None
    # old  code_interpreter: Optional[ToolResourcesCodeInterpreter] = None
    # old  code_interpreter: Optional[ToolResourcesCodeInterpreter] = None
    # old  code_interpreter: Optional[ToolResourcesCodeInterpreter] = None
    # old  code_interpreter: Optional[ToolResourcesCodeInterpreter] = None
    # old  code_interpreter: Optional[ToolResourcesCodeInterpreter] = None
    # old  code_interpreter: ToolResourcesCodeInterpreter

    file_search: Optional[ToolResourcesFileSearch] = None
    # old  file_search: Optional[ToolResourcesFileSearch] = None
    # old  file_search: Optional[ToolResourcesFileSearch] = None
    # old  file_search: Optional[ToolResourcesFileSearch] = None
    # old  file_search: Optional[ToolResourcesFileSearch] = None
    # old  file_search: Optional[ToolResourcesFileSearch] = None
    # old  file_search: Optional[ToolResourcesFileSearch] = None
    # old  file_search: Optional[ToolResourcesFileSearch] = None
    # old  file_search: Optional[ToolResourcesFileSearch] = None
    # old  file_search: Optional[ToolResourcesFileSearch] = None
    # old  file_search: Optional[ToolResourcesFileSearch] = None
    # old  file_search: ToolResourcesFileSearch












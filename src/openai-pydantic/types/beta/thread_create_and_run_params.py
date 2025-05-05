# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union, Iterable, Optional
from typing_extensions import Literal
from pydantic import BaseModel
from ..shared.chat_model import ChatModel
from .assistant_tool_param import AssistantToolParam
from ..shared_params.metadata import Metadata
from .code_interpreter_tool_param import CodeInterpreterToolParam
from .assistant_tool_choice_option_param import AssistantToolChoiceOptionParam
from .threads.message_content_part_param import MessageContentPartParam
from .assistant_response_format_option_param import AssistantResponseFormatOptionParam

__all__ = [
    "ThreadCreateAndRunParamsBase",
    "Thread",
    "ThreadMessage",
    "ThreadMessageAttachment",
    "ThreadMessageAttachmentTool",
    "ThreadMessageAttachmentToolFileSearch",
    "ThreadToolResources",
    "ThreadToolResourcesCodeInterpreter",
    "ThreadToolResourcesFileSearch",
    "ThreadToolResourcesFileSearchVectorStore",
    "ThreadToolResourcesFileSearchVectorStoreChunkingStrategy",
    "ThreadToolResourcesFileSearchVectorStoreChunkingStrategyAuto",
    "ThreadToolResourcesFileSearchVectorStoreChunkingStrategyStatic",
    "ThreadToolResourcesFileSearchVectorStoreChunkingStrategyStaticStatic",
    "ToolResources",
    "ToolResourcesCodeInterpreter",
    "ToolResourcesFileSearch",
    "TruncationStrategy",
    "ThreadCreateAndRunParamsNonStreaming",
    "ThreadCreateAndRunParamsStreaming",
]


class ThreadCreateAndRunParamsBase(BaseModel):
    assistant_id: Optional[str] = None
    # old  assistant_id: Optional[str] = None
    # old  assistant_id: Optional[str] = None
    # old  assistant_id: Optional[str] = None
    # old  assistant_id: Optional[str] = None
    # old  assistant_id: Optional[str] = None
    # old  assistant_id: Optional[str] = None
    # old  assistant_id: Optional[str] = None
    # old  assistant_id: Optional[str] = None
    # old  assistant_id: Optional[str] = None
    # old  assistant_id: Optional[str] = None
    # old  assistant_id: Optional[str] = None
    # old  assistant_id: Optional[str] = None
    # old  assistant_id: Optional[str] = None
    # old  assistant_id: Optional[str] = None
    # old  assistant_id: str = None
    # old  assistant_id: Required[str]
    """
    The ID of the
    [assistant](https://platform.openai.com/docs/api-reference/assistants) to use to
    execute this run.
    """

    instructions: Optional[str] = None
    # old  instructions: Optional[str] = None
    # old  instructions: Optional[str] = None
    # old  instructions: Optional[str] = None
    # old  instructions: Optional[str] = None
    # old  instructions: Optional[str] = None
    # old  instructions: Optional[str] = None
    # old  instructions: Optional[str] = None
    # old  instructions: Optional[str] = None
    # old  instructions: Optional[str] = None
    # old  instructions: Optional[str] = None
    # old  instructions: Optional[str] = None
    # old  instructions: Optional[str] = None
    # old  instructions: Optional[str] = None
    # old  instructions: Optional[str] = None
    # old  instructions: Optional[str] = None
    # old  instructions: Optional[str]
    """Override the default system message of the assistant.

    This is useful for modifying the behavior on a per-run basis.
    """

    max_completion_tokens: Optional[int] = None
    # old  max_completion_tokens: Optional[int] = None
    # old  max_completion_tokens: Optional[int] = None
    # old  max_completion_tokens: Optional[int] = None
    # old  max_completion_tokens: Optional[int] = None
    # old  max_completion_tokens: Optional[int] = None
    # old  max_completion_tokens: Optional[int] = None
    # old  max_completion_tokens: Optional[int] = None
    # old  max_completion_tokens: Optional[int] = None
    # old  max_completion_tokens: Optional[int] = None
    # old  max_completion_tokens: Optional[int] = None
    # old  max_completion_tokens: Optional[int] = None
    # old  max_completion_tokens: Optional[int] = None
    # old  max_completion_tokens: Optional[int] = None
    # old  max_completion_tokens: Optional[int] = None
    # old  max_completion_tokens: Optional[int] = None
    # old  max_completion_tokens: Optional[int]
    """
    The maximum number of completion tokens that may be used over the course of the
    run. The run will make a best effort to use only the number of completion tokens
    specified, across multiple turns of the run. If the run exceeds the number of
    completion tokens specified, the run will end with status `incomplete`. See
    `incomplete_details` for more info.
    """

    max_prompt_tokens: Optional[int] = None
    # old  max_prompt_tokens: Optional[int] = None
    # old  max_prompt_tokens: Optional[int] = None
    # old  max_prompt_tokens: Optional[int] = None
    # old  max_prompt_tokens: Optional[int] = None
    # old  max_prompt_tokens: Optional[int] = None
    # old  max_prompt_tokens: Optional[int] = None
    # old  max_prompt_tokens: Optional[int] = None
    # old  max_prompt_tokens: Optional[int] = None
    # old  max_prompt_tokens: Optional[int] = None
    # old  max_prompt_tokens: Optional[int] = None
    # old  max_prompt_tokens: Optional[int] = None
    # old  max_prompt_tokens: Optional[int] = None
    # old  max_prompt_tokens: Optional[int] = None
    # old  max_prompt_tokens: Optional[int] = None
    # old  max_prompt_tokens: Optional[int] = None
    # old  max_prompt_tokens: Optional[int]
    """The maximum number of prompt tokens that may be used over the course of the run.

    The run will make a best effort to use only the number of prompt tokens
    specified, across multiple turns of the run. If the run exceeds the number of
    prompt tokens specified, the run will end with status `incomplete`. See
    `incomplete_details` for more info.
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

    model: Optional[Union[str, ChatModel, None]] = None
    # old  model: Optional[Union[str, ChatModel, None]] = None
    # old  model: Optional[Union[str, ChatModel, None]] = None
    # old  model: Optional[Union[str, ChatModel, None]] = None
    # old  model: Optional[Union[str, ChatModel, None]] = None
    # old  model: Optional[Union[str, ChatModel, None]] = None
    # old  model: Optional[Union[str, ChatModel, None]] = None
    # old  model: Optional[Union[str, ChatModel, None]] = None
    # old  model: Optional[Union[str, ChatModel, None]] = None
    # old  model: Optional[Union[str, ChatModel, None]] = None
    # old  model: Optional[Union[str, ChatModel, None]] = None
    # old  model: Optional[Union[str, ChatModel, None]] = None
    # old  model: Optional[Union[str, ChatModel, None]] = None
    # old  model: Optional[Union[str, ChatModel, None]] = None
    # old  model: Optional[Union[str, ChatModel, None]] = None
    # old  model: Optional[Union[str, ChatModel, None]] = None
    # old  model: Union[str, ChatModel, None]
    """
    The ID of the [Model](https://platform.openai.com/docs/api-reference/models) to
    be used to execute this run. If a value is provided here, it will override the
    model associated with the assistant. If not, the model associated with the
    assistant will be used.
    """

    parallel_tool_calls: Optional[bool] = None
    # old  parallel_tool_calls: Optional[bool] = None
    # old  parallel_tool_calls: Optional[bool] = None
    # old  parallel_tool_calls: Optional[bool] = None
    # old  parallel_tool_calls: Optional[bool] = None
    # old  parallel_tool_calls: Optional[bool] = None
    # old  parallel_tool_calls: Optional[bool] = None
    # old  parallel_tool_calls: Optional[bool] = None
    # old  parallel_tool_calls: Optional[bool] = None
    # old  parallel_tool_calls: Optional[bool] = None
    # old  parallel_tool_calls: Optional[bool] = None
    # old  parallel_tool_calls: Optional[bool] = None
    # old  parallel_tool_calls: Optional[bool] = None
    # old  parallel_tool_calls: Optional[bool] = None
    # old  parallel_tool_calls: Optional[bool] = None
    # old  parallel_tool_calls: Optional[bool] = None
    # old  parallel_tool_calls: bool
    """
    Whether to enable
    [parallel function calling](https://platform.openai.com/docs/guides/function-calling#configuring-parallel-function-calling)
    during tool use.
    """

    response_format: Optional[AssistantResponseFormatOptionParam] = None
    # old  response_format: Optional[AssistantResponseFormatOptionParam] = None
    # old  response_format: Optional[AssistantResponseFormatOptionParam] = None
    # old  response_format: Optional[AssistantResponseFormatOptionParam] = None
    # old  response_format: Optional[AssistantResponseFormatOptionParam] = None
    # old  response_format: Optional[AssistantResponseFormatOptionParam] = None
    # old  response_format: Optional[AssistantResponseFormatOptionParam] = None
    # old  response_format: Optional[AssistantResponseFormatOptionParam] = None
    # old  response_format: Optional[AssistantResponseFormatOptionParam] = None
    # old  response_format: Optional[AssistantResponseFormatOptionParam] = None
    # old  response_format: Optional[AssistantResponseFormatOptionParam] = None
    # old  response_format: Optional[AssistantResponseFormatOptionParam] = None
    # old  response_format: Optional[AssistantResponseFormatOptionParam] = None
    # old  response_format: Optional[AssistantResponseFormatOptionParam] = None
    # old  response_format: Optional[AssistantResponseFormatOptionParam] = None
    # old  response_format: Optional[AssistantResponseFormatOptionParam] = None
    # old  response_format: Optional[AssistantResponseFormatOptionParam]
    """Specifies the format that the model must output.

    Compatible with [GPT-4o](https://platform.openai.com/docs/models#gpt-4o),
    [GPT-4 Turbo](https://platform.openai.com/docs/models#gpt-4-turbo-and-gpt-4),
    and all GPT-3.5 Turbo models since `gpt-3.5-turbo-1106`.

    Setting to `{ "type": "json_schema", "json_schema": {...} }` enables Structured
    Outputs which ensures the model will match your supplied JSON schema. Learn more
    in the
    [Structured Outputs guide](https://platform.openai.com/docs/guides/structured-outputs).

    Setting to `{ "type": "json_object" }` enables JSON mode, which ensures the
    message the model generates is valid JSON.

    **Important:** when using JSON mode, you **must** also instruct the model to
    produce JSON yourself via a system or user message. Without this, the model may
    generate an unending stream of whitespace until the generation reaches the token
    limit, resulting in a long-running and seemingly "stuck" request. Also note that
    the message content may be partially cut off if `finish_reason="length"`, which
    indicates the generation exceeded `max_tokens` or the conversation exceeded the
    max context length.
    """

    temperature: Optional[float] = None
    # old  temperature: Optional[float] = None
    # old  temperature: Optional[float] = None
    # old  temperature: Optional[float] = None
    # old  temperature: Optional[float] = None
    # old  temperature: Optional[float] = None
    # old  temperature: Optional[float] = None
    # old  temperature: Optional[float] = None
    # old  temperature: Optional[float] = None
    # old  temperature: Optional[float] = None
    # old  temperature: Optional[float] = None
    # old  temperature: Optional[float] = None
    # old  temperature: Optional[float] = None
    # old  temperature: Optional[float] = None
    # old  temperature: Optional[float] = None
    # old  temperature: Optional[float] = None
    # old  temperature: Optional[float]
    """What sampling temperature to use, between 0 and 2.

    Higher values like 0.8 will make the output more random, while lower values like
    0.2 will make it more focused and deterministic.
    """

    thread: Optional[Thread] = None
    # old  thread: Optional[Thread] = None
    # old  thread: Optional[Thread] = None
    # old  thread: Optional[Thread] = None
    # old  thread: Optional[Thread] = None
    # old  thread: Optional[Thread] = None
    # old  thread: Optional[Thread] = None
    # old  thread: Optional[Thread] = None
    # old  thread: Optional[Thread] = None
    # old  thread: Optional[Thread] = None
    # old  thread: Optional[Thread] = None
    # old  thread: Optional[Thread] = None
    # old  thread: Optional[Thread] = None
    # old  thread: Optional[Thread] = None
    # old  thread: Optional[Thread] = None
    # old  thread: Optional[Thread] = None
    # old  thread: Thread
    """Options to create a new thread.

    If no thread is provided when running a request, an empty thread will be
    created.
    """

    tool_choice: Optional[AssistantToolChoiceOptionParam] = None
    # old  tool_choice: Optional[AssistantToolChoiceOptionParam] = None
    # old  tool_choice: Optional[AssistantToolChoiceOptionParam] = None
    # old  tool_choice: Optional[AssistantToolChoiceOptionParam] = None
    # old  tool_choice: Optional[AssistantToolChoiceOptionParam] = None
    # old  tool_choice: Optional[AssistantToolChoiceOptionParam] = None
    # old  tool_choice: Optional[AssistantToolChoiceOptionParam] = None
    # old  tool_choice: Optional[AssistantToolChoiceOptionParam] = None
    # old  tool_choice: Optional[AssistantToolChoiceOptionParam] = None
    # old  tool_choice: Optional[AssistantToolChoiceOptionParam] = None
    # old  tool_choice: Optional[AssistantToolChoiceOptionParam] = None
    # old  tool_choice: Optional[AssistantToolChoiceOptionParam] = None
    # old  tool_choice: Optional[AssistantToolChoiceOptionParam] = None
    # old  tool_choice: Optional[AssistantToolChoiceOptionParam] = None
    # old  tool_choice: Optional[AssistantToolChoiceOptionParam] = None
    # old  tool_choice: Optional[AssistantToolChoiceOptionParam] = None
    # old  tool_choice: Optional[AssistantToolChoiceOptionParam]
    """
    Controls which (if any) tool is called by the model. `none` means the model will
    not call any tools and instead generates a message. `auto` is the default value
    and means the model can pick between generating a message or calling one or more
    tools. `required` means the model must call one or more tools before responding
    to the user. Specifying a particular tool like `{"type": "file_search"}` or
    `{"type": "function", "function": {"name": "my_function"}}` forces the model to
    call that tool.
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
    # old  tool_resources: Optional[ToolResources] = None
    # old  tool_resources: Optional[ToolResources] = None
    # old  tool_resources: Optional[ToolResources] = None
    # old  tool_resources: Optional[ToolResources] = None
    # old  tool_resources: Optional[ToolResources] = None
    # old  tool_resources: Optional[ToolResources]
    """A set of resources that are used by the assistant's tools.

    The resources are specific to the type of tool. For example, the
    `code_interpreter` tool requires a list of file IDs, while the `file_search`
    tool requires a list of vector store IDs.
    """

    tools: Optional[List[AssistantToolParam]] = None
    # old  tools: Optional[List[AssistantToolParam]] = None
    # old  tools: Optional[List[AssistantToolParam]] = None
    # old  tools: Optional[List[AssistantToolParam]] = None
    # old  tools: Optional[List[AssistantToolParam]] = None
    # old  tools: Optional[List[AssistantToolParam]] = None
    # old  tools: Optional[List[AssistantToolParam]] = None
    # old  tools: Optional[List[AssistantToolParam]] = None
    # old  tools: Optional[List[AssistantToolParam]] = None
    # old  tools: Optional[List[AssistantToolParam]] = None
    # old  tools: Optional[List[AssistantToolParam]] = None
    # old  tools: Optional[List[AssistantToolParam]] = None
    # old  tools: Optional[List[AssistantToolParam]] = None
    # old  tools: Optional[List[AssistantToolParam]] = None
    # old  tools: Optional[List[AssistantToolParam]] = None
    # old  tools: Optional[List[AssistantToolParam]] = None
    # old  tools: Optional[Iterable[AssistantToolParam]]
    """Override the tools the assistant can use for this run.

    This is useful for modifying the behavior on a per-run basis.
    """

    top_p: Optional[float] = None
    # old  top_p: Optional[float] = None
    # old  top_p: Optional[float] = None
    # old  top_p: Optional[float] = None
    # old  top_p: Optional[float] = None
    # old  top_p: Optional[float] = None
    # old  top_p: Optional[float] = None
    # old  top_p: Optional[float] = None
    # old  top_p: Optional[float] = None
    # old  top_p: Optional[float] = None
    # old  top_p: Optional[float] = None
    # old  top_p: Optional[float] = None
    # old  top_p: Optional[float] = None
    # old  top_p: Optional[float] = None
    # old  top_p: Optional[float] = None
    # old  top_p: Optional[float] = None
    # old  top_p: Optional[float]
    """
    An alternative to sampling with temperature, called nucleus sampling, where the
    model considers the results of the tokens with top_p probability mass. So 0.1
    means only the tokens comprising the top 10% probability mass are considered.

    We generally recommend altering this or temperature but not both.
    """

    truncation_strategy: Optional[TruncationStrategy] = None
    # old  truncation_strategy: Optional[TruncationStrategy] = None
    # old  truncation_strategy: Optional[TruncationStrategy] = None
    # old  truncation_strategy: Optional[TruncationStrategy] = None
    # old  truncation_strategy: Optional[TruncationStrategy] = None
    # old  truncation_strategy: Optional[TruncationStrategy] = None
    # old  truncation_strategy: Optional[TruncationStrategy] = None
    # old  truncation_strategy: Optional[TruncationStrategy] = None
    # old  truncation_strategy: Optional[TruncationStrategy] = None
    # old  truncation_strategy: Optional[TruncationStrategy] = None
    # old  truncation_strategy: Optional[TruncationStrategy] = None
    # old  truncation_strategy: Optional[TruncationStrategy] = None
    # old  truncation_strategy: Optional[TruncationStrategy] = None
    # old  truncation_strategy: Optional[TruncationStrategy] = None
    # old  truncation_strategy: Optional[TruncationStrategy] = None
    # old  truncation_strategy: Optional[TruncationStrategy] = None
    # old  truncation_strategy: Optional[TruncationStrategy]
    """Controls for how a thread will be truncated prior to the run.

    Use this to control the intial context window of the run.
    """


class ThreadMessageAttachmentToolFileSearch(BaseModel):
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
    # old  type: Optional[Literal["file_search"]] = None
    # old  type: Optional[Literal["file_search"]] = None
    # old  type: Optional[Literal["file_search"]] = None
    # old  type: Optional[Literal["file_search"]] = None
    # old  type: Optional[Literal["file_search"]] = None
    # old  type: Literal["file_search"] = None
    # old  type: Required[Literal["file_search"]]
    """The type of tool being defined: `file_search`"""


ThreadMessageAttachmentTool = Union[CodeInterpreterToolParam, ThreadMessageAttachmentToolFileSearch] # old ThreadMessageAttachmentTool: TypeAlias = Union[CodeInterpreterToolParam, ThreadMessageAttachmentToolFileSearch]


class ThreadMessageAttachment(BaseModel):
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
    # old  file_id: Optional[str] = None
    # old  file_id: Optional[str] = None
    # old  file_id: Optional[str] = None
    # old  file_id: Optional[str] = None
    # old  file_id: Optional[str] = None
    # old  file_id: str
    """The ID of the file to attach to the message."""

    tools: Optional[List[ThreadMessageAttachmentTool]] = None
    # old  tools: Optional[List[ThreadMessageAttachmentTool]] = None
    # old  tools: Optional[List[ThreadMessageAttachmentTool]] = None
    # old  tools: Optional[List[ThreadMessageAttachmentTool]] = None
    # old  tools: Optional[List[ThreadMessageAttachmentTool]] = None
    # old  tools: Optional[List[ThreadMessageAttachmentTool]] = None
    # old  tools: Optional[List[ThreadMessageAttachmentTool]] = None
    # old  tools: Optional[List[ThreadMessageAttachmentTool]] = None
    # old  tools: Optional[List[ThreadMessageAttachmentTool]] = None
    # old  tools: Optional[List[ThreadMessageAttachmentTool]] = None
    # old  tools: Optional[List[ThreadMessageAttachmentTool]] = None
    # old  tools: Optional[List[ThreadMessageAttachmentTool]] = None
    # old  tools: Optional[List[ThreadMessageAttachmentTool]] = None
    # old  tools: Optional[List[ThreadMessageAttachmentTool]] = None
    # old  tools: Optional[List[ThreadMessageAttachmentTool]] = None
    # old  tools: Optional[List[ThreadMessageAttachmentTool]] = None
    # old  tools: Iterable[ThreadMessageAttachmentTool]
    """The tools to add this file to."""


class ThreadMessage(BaseModel):
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

    attachments: Optional[List[ThreadMessageAttachment]] = None
    # old  attachments: Optional[List[ThreadMessageAttachment]] = None
    # old  attachments: Optional[List[ThreadMessageAttachment]] = None
    # old  attachments: Optional[List[ThreadMessageAttachment]] = None
    # old  attachments: Optional[List[ThreadMessageAttachment]] = None
    # old  attachments: Optional[List[ThreadMessageAttachment]] = None
    # old  attachments: Optional[List[ThreadMessageAttachment]] = None
    # old  attachments: Optional[List[ThreadMessageAttachment]] = None
    # old  attachments: Optional[List[ThreadMessageAttachment]] = None
    # old  attachments: Optional[List[ThreadMessageAttachment]] = None
    # old  attachments: Optional[List[ThreadMessageAttachment]] = None
    # old  attachments: Optional[List[ThreadMessageAttachment]] = None
    # old  attachments: Optional[List[ThreadMessageAttachment]] = None
    # old  attachments: Optional[List[ThreadMessageAttachment]] = None
    # old  attachments: Optional[List[ThreadMessageAttachment]] = None
    # old  attachments: Optional[List[ThreadMessageAttachment]] = None
    # old  attachments: Optional[Iterable[ThreadMessageAttachment]]
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


class ThreadToolResourcesCodeInterpreter(BaseModel):
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


class ThreadToolResourcesFileSearchVectorStoreChunkingStrategyAuto(BaseModel):
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
    # old  type: Optional[Literal["auto"]] = None
    # old  type: Optional[Literal["auto"]] = None
    # old  type: Optional[Literal["auto"]] = None
    # old  type: Optional[Literal["auto"]] = None
    # old  type: Optional[Literal["auto"]] = None
    # old  type: Literal["auto"] = None
    # old  type: Required[Literal["auto"]]
    """Always `auto`."""


class ThreadToolResourcesFileSearchVectorStoreChunkingStrategyStaticStatic(BaseModel):
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


class ThreadToolResourcesFileSearchVectorStoreChunkingStrategyStatic(BaseModel):
    static: Optional[ThreadToolResourcesFileSearchVectorStoreChunkingStrategyStaticStatic] = None
    # old  static: Optional[ThreadToolResourcesFileSearchVectorStoreChunkingStrategyStaticStatic] = None
    # old  static: Optional[ThreadToolResourcesFileSearchVectorStoreChunkingStrategyStaticStatic] = None
    # old  static: Optional[ThreadToolResourcesFileSearchVectorStoreChunkingStrategyStaticStatic] = None
    # old  static: Optional[ThreadToolResourcesFileSearchVectorStoreChunkingStrategyStaticStatic] = None
    # old  static: Optional[ThreadToolResourcesFileSearchVectorStoreChunkingStrategyStaticStatic] = None
    # old  static: Optional[ThreadToolResourcesFileSearchVectorStoreChunkingStrategyStaticStatic] = None
    # old  static: Optional[ThreadToolResourcesFileSearchVectorStoreChunkingStrategyStaticStatic] = None
    # old  static: Optional[ThreadToolResourcesFileSearchVectorStoreChunkingStrategyStaticStatic] = None
    # old  static: Optional[ThreadToolResourcesFileSearchVectorStoreChunkingStrategyStaticStatic] = None
    # old  static: Optional[ThreadToolResourcesFileSearchVectorStoreChunkingStrategyStaticStatic] = None
    # old  static: Optional[ThreadToolResourcesFileSearchVectorStoreChunkingStrategyStaticStatic] = None
    # old  static: Optional[ThreadToolResourcesFileSearchVectorStoreChunkingStrategyStaticStatic] = None
    # old  static: Optional[ThreadToolResourcesFileSearchVectorStoreChunkingStrategyStaticStatic] = None
    # old  static: Optional[ThreadToolResourcesFileSearchVectorStoreChunkingStrategyStaticStatic] = None
    # old  static: ThreadToolResourcesFileSearchVectorStoreChunkingStrategyStaticStatic = None
    # old  static: Required[ThreadToolResourcesFileSearchVectorStoreChunkingStrategyStaticStatic]

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
    # old  type: Optional[Literal["static"]] = None
    # old  type: Optional[Literal["static"]] = None
    # old  type: Optional[Literal["static"]] = None
    # old  type: Optional[Literal["static"]] = None
    # old  type: Optional[Literal["static"]] = None
    # old  type: Literal["static"] = None
    # old  type: Required[Literal["static"]]
    """Always `static`."""


ThreadToolResourcesFileSearchVectorStoreChunkingStrategy = Union[ # old ThreadToolResourcesFileSearchVectorStoreChunkingStrategy: TypeAlias = Union[
    ThreadToolResourcesFileSearchVectorStoreChunkingStrategyAuto,
    ThreadToolResourcesFileSearchVectorStoreChunkingStrategyStatic,
]


class ThreadToolResourcesFileSearchVectorStore(BaseModel):
    chunking_strategy: Optional[ThreadToolResourcesFileSearchVectorStoreChunkingStrategy] = None
    # old  chunking_strategy: Optional[ThreadToolResourcesFileSearchVectorStoreChunkingStrategy] = None
    # old  chunking_strategy: Optional[ThreadToolResourcesFileSearchVectorStoreChunkingStrategy] = None
    # old  chunking_strategy: Optional[ThreadToolResourcesFileSearchVectorStoreChunkingStrategy] = None
    # old  chunking_strategy: Optional[ThreadToolResourcesFileSearchVectorStoreChunkingStrategy] = None
    # old  chunking_strategy: Optional[ThreadToolResourcesFileSearchVectorStoreChunkingStrategy] = None
    # old  chunking_strategy: Optional[ThreadToolResourcesFileSearchVectorStoreChunkingStrategy] = None
    # old  chunking_strategy: Optional[ThreadToolResourcesFileSearchVectorStoreChunkingStrategy] = None
    # old  chunking_strategy: Optional[ThreadToolResourcesFileSearchVectorStoreChunkingStrategy] = None
    # old  chunking_strategy: Optional[ThreadToolResourcesFileSearchVectorStoreChunkingStrategy] = None
    # old  chunking_strategy: Optional[ThreadToolResourcesFileSearchVectorStoreChunkingStrategy] = None
    # old  chunking_strategy: Optional[ThreadToolResourcesFileSearchVectorStoreChunkingStrategy] = None
    # old  chunking_strategy: Optional[ThreadToolResourcesFileSearchVectorStoreChunkingStrategy] = None
    # old  chunking_strategy: Optional[ThreadToolResourcesFileSearchVectorStoreChunkingStrategy] = None
    # old  chunking_strategy: Optional[ThreadToolResourcesFileSearchVectorStoreChunkingStrategy] = None
    # old  chunking_strategy: Optional[ThreadToolResourcesFileSearchVectorStoreChunkingStrategy] = None
    # old  chunking_strategy: ThreadToolResourcesFileSearchVectorStoreChunkingStrategy
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


class ThreadToolResourcesFileSearch(BaseModel):
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

    vector_stores: Optional[List[ThreadToolResourcesFileSearchVectorStore]] = None
    # old  vector_stores: Optional[List[ThreadToolResourcesFileSearchVectorStore]] = None
    # old  vector_stores: Optional[List[ThreadToolResourcesFileSearchVectorStore]] = None
    # old  vector_stores: Optional[List[ThreadToolResourcesFileSearchVectorStore]] = None
    # old  vector_stores: Optional[List[ThreadToolResourcesFileSearchVectorStore]] = None
    # old  vector_stores: Optional[List[ThreadToolResourcesFileSearchVectorStore]] = None
    # old  vector_stores: Optional[List[ThreadToolResourcesFileSearchVectorStore]] = None
    # old  vector_stores: Optional[List[ThreadToolResourcesFileSearchVectorStore]] = None
    # old  vector_stores: Optional[List[ThreadToolResourcesFileSearchVectorStore]] = None
    # old  vector_stores: Optional[List[ThreadToolResourcesFileSearchVectorStore]] = None
    # old  vector_stores: Optional[List[ThreadToolResourcesFileSearchVectorStore]] = None
    # old  vector_stores: Optional[List[ThreadToolResourcesFileSearchVectorStore]] = None
    # old  vector_stores: Optional[List[ThreadToolResourcesFileSearchVectorStore]] = None
    # old  vector_stores: Optional[List[ThreadToolResourcesFileSearchVectorStore]] = None
    # old  vector_stores: Optional[List[ThreadToolResourcesFileSearchVectorStore]] = None
    # old  vector_stores: Optional[List[ThreadToolResourcesFileSearchVectorStore]] = None
    # old  vector_stores: Iterable[ThreadToolResourcesFileSearchVectorStore]
    """
    A helper to create a
    [vector store](https://platform.openai.com/docs/api-reference/vector-stores/object)
    with file_ids and attach it to this thread. There can be a maximum of 1 vector
    store attached to the thread.
    """


class ThreadToolResources(BaseModel):
    code_interpreter: Optional[ThreadToolResourcesCodeInterpreter] = None
    # old  code_interpreter: Optional[ThreadToolResourcesCodeInterpreter] = None
    # old  code_interpreter: Optional[ThreadToolResourcesCodeInterpreter] = None
    # old  code_interpreter: Optional[ThreadToolResourcesCodeInterpreter] = None
    # old  code_interpreter: Optional[ThreadToolResourcesCodeInterpreter] = None
    # old  code_interpreter: Optional[ThreadToolResourcesCodeInterpreter] = None
    # old  code_interpreter: Optional[ThreadToolResourcesCodeInterpreter] = None
    # old  code_interpreter: Optional[ThreadToolResourcesCodeInterpreter] = None
    # old  code_interpreter: Optional[ThreadToolResourcesCodeInterpreter] = None
    # old  code_interpreter: Optional[ThreadToolResourcesCodeInterpreter] = None
    # old  code_interpreter: Optional[ThreadToolResourcesCodeInterpreter] = None
    # old  code_interpreter: Optional[ThreadToolResourcesCodeInterpreter] = None
    # old  code_interpreter: Optional[ThreadToolResourcesCodeInterpreter] = None
    # old  code_interpreter: Optional[ThreadToolResourcesCodeInterpreter] = None
    # old  code_interpreter: Optional[ThreadToolResourcesCodeInterpreter] = None
    # old  code_interpreter: Optional[ThreadToolResourcesCodeInterpreter] = None
    # old  code_interpreter: ThreadToolResourcesCodeInterpreter

    file_search: Optional[ThreadToolResourcesFileSearch] = None
    # old  file_search: Optional[ThreadToolResourcesFileSearch] = None
    # old  file_search: Optional[ThreadToolResourcesFileSearch] = None
    # old  file_search: Optional[ThreadToolResourcesFileSearch] = None
    # old  file_search: Optional[ThreadToolResourcesFileSearch] = None
    # old  file_search: Optional[ThreadToolResourcesFileSearch] = None
    # old  file_search: Optional[ThreadToolResourcesFileSearch] = None
    # old  file_search: Optional[ThreadToolResourcesFileSearch] = None
    # old  file_search: Optional[ThreadToolResourcesFileSearch] = None
    # old  file_search: Optional[ThreadToolResourcesFileSearch] = None
    # old  file_search: Optional[ThreadToolResourcesFileSearch] = None
    # old  file_search: Optional[ThreadToolResourcesFileSearch] = None
    # old  file_search: Optional[ThreadToolResourcesFileSearch] = None
    # old  file_search: Optional[ThreadToolResourcesFileSearch] = None
    # old  file_search: Optional[ThreadToolResourcesFileSearch] = None
    # old  file_search: Optional[ThreadToolResourcesFileSearch] = None
    # old  file_search: ThreadToolResourcesFileSearch


class Thread(BaseModel):
    messages: Optional[List[ThreadMessage]] = None
    # old  messages: Optional[List[ThreadMessage]] = None
    # old  messages: Optional[List[ThreadMessage]] = None
    # old  messages: Optional[List[ThreadMessage]] = None
    # old  messages: Optional[List[ThreadMessage]] = None
    # old  messages: Optional[List[ThreadMessage]] = None
    # old  messages: Optional[List[ThreadMessage]] = None
    # old  messages: Optional[List[ThreadMessage]] = None
    # old  messages: Optional[List[ThreadMessage]] = None
    # old  messages: Optional[List[ThreadMessage]] = None
    # old  messages: Optional[List[ThreadMessage]] = None
    # old  messages: Optional[List[ThreadMessage]] = None
    # old  messages: Optional[List[ThreadMessage]] = None
    # old  messages: Optional[List[ThreadMessage]] = None
    # old  messages: Optional[List[ThreadMessage]] = None
    # old  messages: Optional[List[ThreadMessage]] = None
    # old  messages: Iterable[ThreadMessage]
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

    tool_resources: Optional[ThreadToolResources] = None
    # old  tool_resources: Optional[ThreadToolResources] = None
    # old  tool_resources: Optional[ThreadToolResources] = None
    # old  tool_resources: Optional[ThreadToolResources] = None
    # old  tool_resources: Optional[ThreadToolResources] = None
    # old  tool_resources: Optional[ThreadToolResources] = None
    # old  tool_resources: Optional[ThreadToolResources] = None
    # old  tool_resources: Optional[ThreadToolResources] = None
    # old  tool_resources: Optional[ThreadToolResources] = None
    # old  tool_resources: Optional[ThreadToolResources] = None
    # old  tool_resources: Optional[ThreadToolResources] = None
    # old  tool_resources: Optional[ThreadToolResources] = None
    # old  tool_resources: Optional[ThreadToolResources] = None
    # old  tool_resources: Optional[ThreadToolResources] = None
    # old  tool_resources: Optional[ThreadToolResources] = None
    # old  tool_resources: Optional[ThreadToolResources] = None
    # old  tool_resources: Optional[ThreadToolResources]
    """
    A set of resources that are made available to the assistant's tools in this
    thread. The resources are specific to the type of tool. For example, the
    `code_interpreter` tool requires a list of file IDs, while the `file_search`
    tool requires a list of vector store IDs.
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
    # old  vector_store_ids: Optional[List[str]] = None
    # old  vector_store_ids: Optional[List[str]] = None
    # old  vector_store_ids: Optional[List[str]] = None
    # old  vector_store_ids: Optional[List[str]] = None
    # old  vector_store_ids: Optional[List[str]] = None
    # old  vector_store_ids: List[str]
    """
    The ID of the
    [vector store](https://platform.openai.com/docs/api-reference/vector-stores/object)
    attached to this assistant. There can be a maximum of 1 vector store attached to
    the assistant.
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
    # old  file_search: Optional[ToolResourcesFileSearch] = None
    # old  file_search: Optional[ToolResourcesFileSearch] = None
    # old  file_search: Optional[ToolResourcesFileSearch] = None
    # old  file_search: Optional[ToolResourcesFileSearch] = None
    # old  file_search: Optional[ToolResourcesFileSearch] = None
    # old  file_search: ToolResourcesFileSearch


class TruncationStrategy(BaseModel):
    type: Optional[Literal["auto", "last_messages"]] = None
    # old  type: Optional[Literal["auto", "last_messages"]] = None
    # old  type: Optional[Literal["auto", "last_messages"]] = None
    # old  type: Optional[Literal["auto", "last_messages"]] = None
    # old  type: Optional[Literal["auto", "last_messages"]] = None
    # old  type: Optional[Literal["auto", "last_messages"]] = None
    # old  type: Optional[Literal["auto", "last_messages"]] = None
    # old  type: Optional[Literal["auto", "last_messages"]] = None
    # old  type: Optional[Literal["auto", "last_messages"]] = None
    # old  type: Optional[Literal["auto", "last_messages"]] = None
    # old  type: Optional[Literal["auto", "last_messages"]] = None
    # old  type: Optional[Literal["auto", "last_messages"]] = None
    # old  type: Optional[Literal["auto", "last_messages"]] = None
    # old  type: Optional[Literal["auto", "last_messages"]] = None
    # old  type: Optional[Literal["auto", "last_messages"]] = None
    # old  type: Literal["auto", "last_messages"] = None
    # old  type: Required[Literal["auto", "last_messages"]]
    """The truncation strategy to use for the thread.

    The default is `auto`. If set to `last_messages`, the thread will be truncated
    to the n most recent messages in the thread. When set to `auto`, messages in the
    middle of the thread will be dropped to fit the context length of the model,
    `max_prompt_tokens`.
    """

    last_messages: Optional[int] = None
    # old  last_messages: Optional[int] = None
    # old  last_messages: Optional[int] = None
    # old  last_messages: Optional[int] = None
    # old  last_messages: Optional[int] = None
    # old  last_messages: Optional[int] = None
    # old  last_messages: Optional[int] = None
    # old  last_messages: Optional[int] = None
    # old  last_messages: Optional[int] = None
    # old  last_messages: Optional[int] = None
    # old  last_messages: Optional[int] = None
    # old  last_messages: Optional[int] = None
    # old  last_messages: Optional[int] = None
    # old  last_messages: Optional[int] = None
    # old  last_messages: Optional[int] = None
    # old  last_messages: Optional[int] = None
    # old  last_messages: Optional[int]
    """
    The number of most recent messages from the thread when constructing the context
    for the run.
    """


class ThreadCreateAndRunParamsNonStreaming(ThreadCreateAndRunParamsBase):
    stream: Optional[Literal[False]] = None
    # old  stream: Optional[Literal[False]] = None
    # old  stream: Optional[Literal[False]] = None
    # old  stream: Optional[Literal[False]] = None
    # old  stream: Optional[Literal[False]] = None
    # old  stream: Optional[Literal[False]] = None
    # old  stream: Optional[Literal[False]] = None
    # old  stream: Optional[Literal[False]] = None
    # old  stream: Optional[Literal[False]] = None
    # old  stream: Optional[Literal[False]] = None
    # old  stream: Optional[Literal[False]] = None
    # old  stream: Optional[Literal[False]] = None
    # old  stream: Optional[Literal[False]] = None
    # old  stream: Optional[Literal[False]] = None
    # old  stream: Optional[Literal[False]] = None
    # old  stream: Optional[Literal[False]] = None
    # old  stream: Optional[Literal[False]]
    """
    If `true`, returns a stream of events that happen during the Run as server-sent
    events, terminating when the Run enters a terminal state with a `data: [DONE]`
    message.
    """


class ThreadCreateAndRunParamsStreaming(ThreadCreateAndRunParamsBase):
    stream: Optional[Literal[True]] = None
    # old  stream: Optional[Literal[True]] = None
    # old  stream: Optional[Literal[True]] = None
    # old  stream: Optional[Literal[True]] = None
    # old  stream: Optional[Literal[True]] = None
    # old  stream: Optional[Literal[True]] = None
    # old  stream: Optional[Literal[True]] = None
    # old  stream: Optional[Literal[True]] = None
    # old  stream: Optional[Literal[True]] = None
    # old  stream: Optional[Literal[True]] = None
    # old  stream: Optional[Literal[True]] = None
    # old  stream: Optional[Literal[True]] = None
    # old  stream: Optional[Literal[True]] = None
    # old  stream: Optional[Literal[True]] = None
    # old  stream: Optional[Literal[True]] = None
    # old  stream: Literal[True] = None
    # old  stream: Required[Literal[True]]
    """
    If `true`, returns a stream of events that happen during the Run as server-sent
    events, terminating when the Run enters a terminal state with a `data: [DONE]`
    message.
    """


ThreadCreateAndRunParams = Union[ThreadCreateAndRunParamsNonStreaming, ThreadCreateAndRunParamsStreaming]

















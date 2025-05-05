# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Iterable, Optional
from typing_extensions import Literal
from pydantic import BaseModel
from ..shared_params.metadata import Metadata
from ..responses.easy_input_message_param import EasyInputMessageParam
from ..responses.response_input_text_param import ResponseInputTextParam

__all__ = [
    "CreateEvalCompletionsRunDataSourceParam",
    "Source",
    "SourceFileContent",
    "SourceFileContentContent",
    "SourceFileID",
    "SourceStoredCompletions",
    "InputMessages",
    "InputMessagesTemplate",
    "InputMessagesTemplateTemplate",
    "InputMessagesTemplateTemplateMessage",
    "InputMessagesTemplateTemplateMessageContent",
    "InputMessagesTemplateTemplateMessageContentOutputText",
    "InputMessagesItemReference",
    "SamplingParams",
]


class SourceFileContentContent(BaseModel):
    item: Optional[Dict[str, object]] = None
    # old  item: Optional[Dict[str, object]] = None
    # old  item: Optional[Dict[str, object]] = None
    # old  item: Optional[Dict[str, object]] = None
    # old  item: Optional[Dict[str, object]] = None
    # old  item: Optional[Dict[str, object]] = None
    # old  item: Optional[Dict[str, object]] = None
    # old  item: Optional[Dict[str, object]] = None
    # old  item: Optional[Dict[str, object]] = None
    # old  item: Dict[str, object] = None
    # old  item: Required[Dict[str, object]]

    sample: Optional[Dict[str, object]] = None
    # old  sample: Optional[Dict[str, object]] = None
    # old  sample: Optional[Dict[str, object]] = None
    # old  sample: Optional[Dict[str, object]] = None
    # old  sample: Optional[Dict[str, object]] = None
    # old  sample: Optional[Dict[str, object]] = None
    # old  sample: Optional[Dict[str, object]] = None
    # old  sample: Optional[Dict[str, object]] = None
    # old  sample: Optional[Dict[str, object]] = None
    # old  sample: Optional[Dict[str, object]] = None
    # old  sample: Dict[str, object]


class SourceFileContent(BaseModel):
    content: Optional[List[SourceFileContentContent]] = None
    # old  content: Optional[List[SourceFileContentContent]] = None
    # old  content: Optional[List[SourceFileContentContent]] = None
    # old  content: Optional[List[SourceFileContentContent]] = None
    # old  content: Optional[List[SourceFileContentContent]] = None
    # old  content: Optional[List[SourceFileContentContent]] = None
    # old  content: Optional[List[SourceFileContentContent]] = None
    # old  content: Optional[List[SourceFileContentContent]] = None
    # old  content: Optional[List[SourceFileContentContent]] = None
    # old  content: List[SourceFileContentContent] = None
    # old  content: Required[Iterable[SourceFileContentContent]]
    """The content of the jsonl file."""

    type: Optional[Literal["file_content"]] = None
    # old  type: Optional[Literal["file_content"]] = None
    # old  type: Optional[Literal["file_content"]] = None
    # old  type: Optional[Literal["file_content"]] = None
    # old  type: Optional[Literal["file_content"]] = None
    # old  type: Optional[Literal["file_content"]] = None
    # old  type: Optional[Literal["file_content"]] = None
    # old  type: Optional[Literal["file_content"]] = None
    # old  type: Optional[Literal["file_content"]] = None
    # old  type: Literal["file_content"] = None
    # old  type: Required[Literal["file_content"]]
    """The type of jsonl source. Always `file_content`."""


class SourceFileID(BaseModel):
    id: Optional[str] = None
    # old  id: Optional[str] = None
    # old  id: Optional[str] = None
    # old  id: Optional[str] = None
    # old  id: Optional[str] = None
    # old  id: Optional[str] = None
    # old  id: Optional[str] = None
    # old  id: Optional[str] = None
    # old  id: Optional[str] = None
    # old  id: str = None
    # old  id: Required[str]
    """The identifier of the file."""

    type: Optional[Literal["file_id"]] = None
    # old  type: Optional[Literal["file_id"]] = None
    # old  type: Optional[Literal["file_id"]] = None
    # old  type: Optional[Literal["file_id"]] = None
    # old  type: Optional[Literal["file_id"]] = None
    # old  type: Optional[Literal["file_id"]] = None
    # old  type: Optional[Literal["file_id"]] = None
    # old  type: Optional[Literal["file_id"]] = None
    # old  type: Optional[Literal["file_id"]] = None
    # old  type: Literal["file_id"] = None
    # old  type: Required[Literal["file_id"]]
    """The type of jsonl source. Always `file_id`."""


class SourceStoredCompletions(BaseModel):
    type: Optional[Literal["stored_completions"]] = None
    # old  type: Optional[Literal["stored_completions"]] = None
    # old  type: Optional[Literal["stored_completions"]] = None
    # old  type: Optional[Literal["stored_completions"]] = None
    # old  type: Optional[Literal["stored_completions"]] = None
    # old  type: Optional[Literal["stored_completions"]] = None
    # old  type: Optional[Literal["stored_completions"]] = None
    # old  type: Optional[Literal["stored_completions"]] = None
    # old  type: Optional[Literal["stored_completions"]] = None
    # old  type: Literal["stored_completions"] = None
    # old  type: Required[Literal["stored_completions"]]
    """The type of source. Always `stored_completions`."""

    created_after: Optional[int] = None
    # old  created_after: Optional[int] = None
    # old  created_after: Optional[int] = None
    # old  created_after: Optional[int] = None
    # old  created_after: Optional[int] = None
    # old  created_after: Optional[int] = None
    # old  created_after: Optional[int] = None
    # old  created_after: Optional[int] = None
    # old  created_after: Optional[int] = None
    # old  created_after: Optional[int] = None
    # old  created_after: Optional[int]
    """An optional Unix timestamp to filter items created after this time."""

    created_before: Optional[int] = None
    # old  created_before: Optional[int] = None
    # old  created_before: Optional[int] = None
    # old  created_before: Optional[int] = None
    # old  created_before: Optional[int] = None
    # old  created_before: Optional[int] = None
    # old  created_before: Optional[int] = None
    # old  created_before: Optional[int] = None
    # old  created_before: Optional[int] = None
    # old  created_before: Optional[int] = None
    # old  created_before: Optional[int]
    """An optional Unix timestamp to filter items created before this time."""

    limit: Optional[int] = None
    # old  limit: Optional[int] = None
    # old  limit: Optional[int] = None
    # old  limit: Optional[int] = None
    # old  limit: Optional[int] = None
    # old  limit: Optional[int] = None
    # old  limit: Optional[int] = None
    # old  limit: Optional[int] = None
    # old  limit: Optional[int] = None
    # old  limit: Optional[int] = None
    # old  limit: Optional[int]
    """An optional maximum number of items to return."""

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
    # old  metadata: Optional[Metadata]
    """Set of 16 key-value pairs that can be attached to an object.

    This can be useful for storing additional information about the object in a
    structured format, and querying for objects via API or the dashboard.

    Keys are strings with a maximum length of 64 characters. Values are strings with
    a maximum length of 512 characters.
    """

    model: Optional[str] = None
    # old  model: Optional[str] = None
    # old  model: Optional[str] = None
    # old  model: Optional[str] = None
    # old  model: Optional[str] = None
    # old  model: Optional[str] = None
    # old  model: Optional[str] = None
    # old  model: Optional[str] = None
    # old  model: Optional[str] = None
    # old  model: Optional[str] = None
    # old  model: Optional[str]
    """An optional model to filter by (e.g., 'gpt-4o')."""


Source = Union[SourceFileContent, SourceFileID, SourceStoredCompletions] # old Source: TypeAlias = Union[SourceFileContent, SourceFileID, SourceStoredCompletions]


class InputMessagesTemplateTemplateMessageContentOutputText(BaseModel):
    text: Optional[str] = None
    # old  text: Optional[str] = None
    # old  text: Optional[str] = None
    # old  text: Optional[str] = None
    # old  text: Optional[str] = None
    # old  text: Optional[str] = None
    # old  text: Optional[str] = None
    # old  text: Optional[str] = None
    # old  text: Optional[str] = None
    # old  text: str = None
    # old  text: Required[str]
    """The text output from the model."""

    type: Optional[Literal["output_text"]] = None
    # old  type: Optional[Literal["output_text"]] = None
    # old  type: Optional[Literal["output_text"]] = None
    # old  type: Optional[Literal["output_text"]] = None
    # old  type: Optional[Literal["output_text"]] = None
    # old  type: Optional[Literal["output_text"]] = None
    # old  type: Optional[Literal["output_text"]] = None
    # old  type: Optional[Literal["output_text"]] = None
    # old  type: Optional[Literal["output_text"]] = None
    # old  type: Literal["output_text"] = None
    # old  type: Required[Literal["output_text"]]
    """The type of the output text. Always `output_text`."""


InputMessagesTemplateTemplateMessageContent = Union[ # old InputMessagesTemplateTemplateMessageContent: TypeAlias = Union[
    str, ResponseInputTextParam, InputMessagesTemplateTemplateMessageContentOutputText
]


class InputMessagesTemplateTemplateMessage(BaseModel):
    content: Optional[InputMessagesTemplateTemplateMessageContent] = None
    # old  content: Optional[InputMessagesTemplateTemplateMessageContent] = None
    # old  content: Optional[InputMessagesTemplateTemplateMessageContent] = None
    # old  content: Optional[InputMessagesTemplateTemplateMessageContent] = None
    # old  content: Optional[InputMessagesTemplateTemplateMessageContent] = None
    # old  content: Optional[InputMessagesTemplateTemplateMessageContent] = None
    # old  content: Optional[InputMessagesTemplateTemplateMessageContent] = None
    # old  content: Optional[InputMessagesTemplateTemplateMessageContent] = None
    # old  content: Optional[InputMessagesTemplateTemplateMessageContent] = None
    # old  content: InputMessagesTemplateTemplateMessageContent = None
    # old  content: Required[InputMessagesTemplateTemplateMessageContent]
    """Text inputs to the model - can contain template strings."""

    role: Optional[Literal["user", "assistant", "system", "developer"]] = None
    # old  role: Optional[Literal["user", "assistant", "system", "developer"]] = None
    # old  role: Optional[Literal["user", "assistant", "system", "developer"]] = None
    # old  role: Optional[Literal["user", "assistant", "system", "developer"]] = None
    # old  role: Optional[Literal["user", "assistant", "system", "developer"]] = None
    # old  role: Optional[Literal["user", "assistant", "system", "developer"]] = None
    # old  role: Optional[Literal["user", "assistant", "system", "developer"]] = None
    # old  role: Optional[Literal["user", "assistant", "system", "developer"]] = None
    # old  role: Optional[Literal["user", "assistant", "system", "developer"]] = None
    # old  role: Literal["user", "assistant", "system", "developer"] = None
    # old  role: Required[Literal["user", "assistant", "system", "developer"]]
    """The role of the message input.

    One of `user`, `assistant`, `system`, or `developer`.
    """

    type: Optional[Literal["message"]] = None
    # old  type: Optional[Literal["message"]] = None
    # old  type: Optional[Literal["message"]] = None
    # old  type: Optional[Literal["message"]] = None
    # old  type: Optional[Literal["message"]] = None
    # old  type: Optional[Literal["message"]] = None
    # old  type: Optional[Literal["message"]] = None
    # old  type: Optional[Literal["message"]] = None
    # old  type: Optional[Literal["message"]] = None
    # old  type: Optional[Literal["message"]] = None
    # old  type: Literal["message"]
    """The type of the message input. Always `message`."""


InputMessagesTemplateTemplate = Union[EasyInputMessageParam, InputMessagesTemplateTemplateMessage] # old InputMessagesTemplateTemplate: TypeAlias = Union[EasyInputMessageParam, InputMessagesTemplateTemplateMessage]


class InputMessagesTemplate(BaseModel):
    template: Optional[List[InputMessagesTemplateTemplate]] = None
    # old  template: Optional[List[InputMessagesTemplateTemplate]] = None
    # old  template: Optional[List[InputMessagesTemplateTemplate]] = None
    # old  template: Optional[List[InputMessagesTemplateTemplate]] = None
    # old  template: Optional[List[InputMessagesTemplateTemplate]] = None
    # old  template: Optional[List[InputMessagesTemplateTemplate]] = None
    # old  template: Optional[List[InputMessagesTemplateTemplate]] = None
    # old  template: Optional[List[InputMessagesTemplateTemplate]] = None
    # old  template: Optional[List[InputMessagesTemplateTemplate]] = None
    # old  template: List[InputMessagesTemplateTemplate] = None
    # old  template: Required[Iterable[InputMessagesTemplateTemplate]]
    """A list of chat messages forming the prompt or context.

    May include variable references to the "item" namespace, ie {{item.name}}.
    """

    type: Optional[Literal["template"]] = None
    # old  type: Optional[Literal["template"]] = None
    # old  type: Optional[Literal["template"]] = None
    # old  type: Optional[Literal["template"]] = None
    # old  type: Optional[Literal["template"]] = None
    # old  type: Optional[Literal["template"]] = None
    # old  type: Optional[Literal["template"]] = None
    # old  type: Optional[Literal["template"]] = None
    # old  type: Optional[Literal["template"]] = None
    # old  type: Literal["template"] = None
    # old  type: Required[Literal["template"]]
    """The type of input messages. Always `template`."""


class InputMessagesItemReference(BaseModel):
    item_reference: Optional[str] = None
    # old  item_reference: Optional[str] = None
    # old  item_reference: Optional[str] = None
    # old  item_reference: Optional[str] = None
    # old  item_reference: Optional[str] = None
    # old  item_reference: Optional[str] = None
    # old  item_reference: Optional[str] = None
    # old  item_reference: Optional[str] = None
    # old  item_reference: Optional[str] = None
    # old  item_reference: str = None
    # old  item_reference: Required[str]
    """A reference to a variable in the "item" namespace. Ie, "item.name" """

    type: Optional[Literal["item_reference"]] = None
    # old  type: Optional[Literal["item_reference"]] = None
    # old  type: Optional[Literal["item_reference"]] = None
    # old  type: Optional[Literal["item_reference"]] = None
    # old  type: Optional[Literal["item_reference"]] = None
    # old  type: Optional[Literal["item_reference"]] = None
    # old  type: Optional[Literal["item_reference"]] = None
    # old  type: Optional[Literal["item_reference"]] = None
    # old  type: Optional[Literal["item_reference"]] = None
    # old  type: Literal["item_reference"] = None
    # old  type: Required[Literal["item_reference"]]
    """The type of input messages. Always `item_reference`."""


InputMessages = Union[InputMessagesTemplate, InputMessagesItemReference] # old InputMessages: TypeAlias = Union[InputMessagesTemplate, InputMessagesItemReference]


class SamplingParams(BaseModel):
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
    # old  max_completion_tokens: int
    """The maximum number of tokens in the generated output."""

    seed: Optional[int] = None
    # old  seed: Optional[int] = None
    # old  seed: Optional[int] = None
    # old  seed: Optional[int] = None
    # old  seed: Optional[int] = None
    # old  seed: Optional[int] = None
    # old  seed: Optional[int] = None
    # old  seed: Optional[int] = None
    # old  seed: Optional[int] = None
    # old  seed: Optional[int] = None
    # old  seed: int
    """A seed value to initialize the randomness, during sampling."""

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
    # old  temperature: float
    """A higher temperature increases randomness in the outputs."""

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
    # old  top_p: float
    """An alternative to temperature for nucleus sampling; 1.0 includes all tokens."""


class CreateEvalCompletionsRunDataSourceParam(BaseModel):
    source: Optional[Source] = None
    # old  source: Optional[Source] = None
    # old  source: Optional[Source] = None
    # old  source: Optional[Source] = None
    # old  source: Optional[Source] = None
    # old  source: Optional[Source] = None
    # old  source: Optional[Source] = None
    # old  source: Optional[Source] = None
    # old  source: Optional[Source] = None
    # old  source: Source = None
    # old  source: Required[Source]
    """A StoredCompletionsRunDataSource configuration describing a set of filters"""

    type: Optional[Literal["completions"]] = None
    # old  type: Optional[Literal["completions"]] = None
    # old  type: Optional[Literal["completions"]] = None
    # old  type: Optional[Literal["completions"]] = None
    # old  type: Optional[Literal["completions"]] = None
    # old  type: Optional[Literal["completions"]] = None
    # old  type: Optional[Literal["completions"]] = None
    # old  type: Optional[Literal["completions"]] = None
    # old  type: Optional[Literal["completions"]] = None
    # old  type: Literal["completions"] = None
    # old  type: Required[Literal["completions"]]
    """The type of run data source. Always `completions`."""

    input_messages: Optional[InputMessages] = None
    # old  input_messages: Optional[InputMessages] = None
    # old  input_messages: Optional[InputMessages] = None
    # old  input_messages: Optional[InputMessages] = None
    # old  input_messages: Optional[InputMessages] = None
    # old  input_messages: Optional[InputMessages] = None
    # old  input_messages: Optional[InputMessages] = None
    # old  input_messages: Optional[InputMessages] = None
    # old  input_messages: Optional[InputMessages] = None
    # old  input_messages: Optional[InputMessages] = None
    # old  input_messages: InputMessages

    model: Optional[str] = None
    # old  model: Optional[str] = None
    # old  model: Optional[str] = None
    # old  model: Optional[str] = None
    # old  model: Optional[str] = None
    # old  model: Optional[str] = None
    # old  model: Optional[str] = None
    # old  model: Optional[str] = None
    # old  model: Optional[str] = None
    # old  model: Optional[str] = None
    # old  model: str
    """The name of the model to use for generating completions (e.g. "o3-mini")."""

    sampling_params: Optional[SamplingParams] = None
    # old  sampling_params: Optional[SamplingParams] = None
    # old  sampling_params: Optional[SamplingParams] = None
    # old  sampling_params: Optional[SamplingParams] = None
    # old  sampling_params: Optional[SamplingParams] = None
    # old  sampling_params: Optional[SamplingParams] = None
    # old  sampling_params: Optional[SamplingParams] = None
    # old  sampling_params: Optional[SamplingParams] = None
    # old  sampling_params: Optional[SamplingParams] = None
    # old  sampling_params: Optional[SamplingParams] = None
    # old  sampling_params: SamplingParams











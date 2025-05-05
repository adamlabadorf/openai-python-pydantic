# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List, Union, Iterable, Optional
from typing_extensions import Literal
from pydantic import BaseModel
from ..shared_params.metadata import Metadata
from ..shared.reasoning_effort import ReasoningEffort
from ..responses.response_input_text_param import ResponseInputTextParam
from .create_eval_jsonl_run_data_source_param import CreateEvalJSONLRunDataSourceParam
from .create_eval_completions_run_data_source_param import CreateEvalCompletionsRunDataSourceParam

__all__ = [
    "RunCreateParams",
    "DataSource",
    "DataSourceCreateEvalResponsesRunDataSource",
    "DataSourceCreateEvalResponsesRunDataSourceSource",
    "DataSourceCreateEvalResponsesRunDataSourceSourceFileContent",
    "DataSourceCreateEvalResponsesRunDataSourceSourceFileContentContent",
    "DataSourceCreateEvalResponsesRunDataSourceSourceFileID",
    "DataSourceCreateEvalResponsesRunDataSourceSourceResponses",
    "DataSourceCreateEvalResponsesRunDataSourceInputMessages",
    "DataSourceCreateEvalResponsesRunDataSourceInputMessagesTemplate",
    "DataSourceCreateEvalResponsesRunDataSourceInputMessagesTemplateTemplate",
    "DataSourceCreateEvalResponsesRunDataSourceInputMessagesTemplateTemplateChatMessage",
    "DataSourceCreateEvalResponsesRunDataSourceInputMessagesTemplateTemplateEvalItem",
    "DataSourceCreateEvalResponsesRunDataSourceInputMessagesTemplateTemplateEvalItemContent",
    "DataSourceCreateEvalResponsesRunDataSourceInputMessagesTemplateTemplateEvalItemContentOutputText",
    "DataSourceCreateEvalResponsesRunDataSourceInputMessagesItemReference",
    "DataSourceCreateEvalResponsesRunDataSourceSamplingParams",
]


class RunCreateParams(BaseModel):
    data_source: Optional[DataSource] = None
    # old  data_source: Required[DataSource]
    """Details about the run's data source."""

    metadata: Optional[Metadata] = None
    # old  metadata: Optional[Metadata]
    """Set of 16 key-value pairs that can be attached to an object.

    This can be useful for storing additional information about the object in a
    structured format, and querying for objects via API or the dashboard.

    Keys are strings with a maximum length of 64 characters. Values are strings with
    a maximum length of 512 characters.
    """

    name: Optional[str] = None
   # old  name: str
    """The name of the run."""


class DataSourceCreateEvalResponsesRunDataSourceSourceFileContentContent(BaseModel):
    item: Optional[Dict[str, object]] = None
   # old  item: Required[Dict[str, object]]

    sample: Optional[Dict[str, object]] = None
   # old  sample: Dict[str, object]


class DataSourceCreateEvalResponsesRunDataSourceSourceFileContent(BaseModel):
    content: Optional[List[DataSourceCreateEvalResponsesRunDataSourceSourceFileContentContent]] = None
   # old  content: Required[Iterable[DataSourceCreateEvalResponsesRunDataSourceSourceFileContentContent]]
    """The content of the jsonl file."""

    type: Optional[Literal["file_content"]] = None
   # old  type: Required[Literal["file_content"]]
    """The type of jsonl source. Always `file_content`."""


class DataSourceCreateEvalResponsesRunDataSourceSourceFileID(BaseModel):
    id: Optional[str] = None
   # old  id: Required[str]
    """The identifier of the file."""

    type: Optional[Literal["file_id"]] = None
   # old  type: Required[Literal["file_id"]]
    """The type of jsonl source. Always `file_id`."""


class DataSourceCreateEvalResponsesRunDataSourceSourceResponses(BaseModel):
    type: Optional[Literal["responses"]] = None
   # old  type: Required[Literal["responses"]]
    """The type of run data source. Always `responses`."""

    allow_parallel_tool_calls: Optional[bool] = None
   # old  allow_parallel_tool_calls: Optional[bool]
    """Whether to allow parallel tool calls.

    This is a query parameter used to select responses.
    """

    created_after: Optional[int] = None
   # old  created_after: Optional[int]
    """Only include items created after this timestamp (inclusive).

    This is a query parameter used to select responses.
    """

    created_before: Optional[int] = None
   # old  created_before: Optional[int]
    """Only include items created before this timestamp (inclusive).

    This is a query parameter used to select responses.
    """

    has_tool_calls: Optional[bool] = None
   # old  has_tool_calls: Optional[bool]
    """Whether the response has tool calls.

    This is a query parameter used to select responses.
    """

    instructions_search: Optional[str] = None
   # old  instructions_search: Optional[str]
    """Optional search string for instructions.

    This is a query parameter used to select responses.
    """

    metadata: Optional[object] = None
   # old  metadata: Optional[object]
    """Metadata filter for the responses.

    This is a query parameter used to select responses.
    """

    model: Optional[str] = None
   # old  model: Optional[str]
    """The name of the model to find responses for.

    This is a query parameter used to select responses.
    """

    reasoning_effort: Optional[ReasoningEffort] = None
   # old  reasoning_effort: Optional[ReasoningEffort]
    """Optional reasoning effort parameter.

    This is a query parameter used to select responses.
    """

    temperature: Optional[float] = None
   # old  temperature: Optional[float]
    """Sampling temperature. This is a query parameter used to select responses."""

    top_p: Optional[float] = None
   # old  top_p: Optional[float]
    """Nucleus sampling parameter. This is a query parameter used to select responses."""

    users: Optional[List[str]] = None
   # old  users: Optional[List[str]]
    """List of user identifiers. This is a query parameter used to select responses."""


DataSourceCreateEvalResponsesRunDataSourceSource = Union[
    DataSourceCreateEvalResponsesRunDataSourceSourceFileContent,
    DataSourceCreateEvalResponsesRunDataSourceSourceFileID,
    DataSourceCreateEvalResponsesRunDataSourceSourceResponses,
]


class DataSourceCreateEvalResponsesRunDataSourceInputMessagesTemplateTemplateChatMessage(BaseModel):
    content: Optional[str] = None
    # old  content: Required[str]
    """The content of the message."""

    role: Optional[str] = None
   # old  role: Required[str]
    """The role of the message (e.g. "system", "assistant", "user")."""


class DataSourceCreateEvalResponsesRunDataSourceInputMessagesTemplateTemplateEvalItemContentOutputText(BaseModel):
    text: Optional[str] = None
   # old  text: Required[str]
    """The text output from the model."""

    type: Optional[Literal["output_text"]] = None
   # old  type: Required[Literal["output_text"]]
    """The type of the output text. Always `output_text`."""


DataSourceCreateEvalResponsesRunDataSourceInputMessagesTemplateTemplateEvalItemContent = Union[
    str,
    ResponseInputTextParam,
    DataSourceCreateEvalResponsesRunDataSourceInputMessagesTemplateTemplateEvalItemContentOutputText,
]


class DataSourceCreateEvalResponsesRunDataSourceInputMessagesTemplateTemplateEvalItem(BaseModel):
    content: Optional[DataSourceCreateEvalResponsesRunDataSourceInputMessagesTemplateTemplateEvalItemContent] = None
   # old  content: Required[DataSourceCreateEvalResponsesRunDataSourceInputMessagesTemplateTemplateEvalItemContent]
    """Text inputs to the model - can contain template strings."""

    role: Optional[Literal["user", "assistant", "system", "developer"]] = None
   # old  role: Required[Literal["user", "assistant", "system", "developer"]]
    """The role of the message input.

    One of `user`, `assistant`, `system`, or `developer`.
    """

    type: Optional[Literal["message"]] = None
   # old  type: Literal["message"]
    """The type of the message input. Always `message`."""


DataSourceCreateEvalResponsesRunDataSourceInputMessagesTemplateTemplate = Union[
    DataSourceCreateEvalResponsesRunDataSourceInputMessagesTemplateTemplateChatMessage,
    DataSourceCreateEvalResponsesRunDataSourceInputMessagesTemplateTemplateEvalItem,
]


class DataSourceCreateEvalResponsesRunDataSourceInputMessagesTemplate(BaseModel):
    template: Optional[List[DataSourceCreateEvalResponsesRunDataSourceInputMessagesTemplateTemplate]] = None
   # old  template: Required[Iterable[DataSourceCreateEvalResponsesRunDataSourceInputMessagesTemplateTemplate]]
    """A list of chat messages forming the prompt or context.

    May include variable references to the "item" namespace, ie {{item.name}}.
    """

    type: Optional[Literal["template"]] = None
   # old  type: Required[Literal["template"]]
    """The type of input messages. Always `template`."""


class DataSourceCreateEvalResponsesRunDataSourceInputMessagesItemReference(BaseModel):
    item_reference: Optional[str] = None
   # old  item_reference: Required[str]
    """A reference to a variable in the "item" namespace. Ie, "item.name" """

    type: Optional[Literal["item_reference"]] = None
   # old  type: Required[Literal["item_reference"]]
    """The type of input messages. Always `item_reference`."""


DataSourceCreateEvalResponsesRunDataSourceInputMessages = Union[
    DataSourceCreateEvalResponsesRunDataSourceInputMessagesTemplate,
    DataSourceCreateEvalResponsesRunDataSourceInputMessagesItemReference,
]


class DataSourceCreateEvalResponsesRunDataSourceSamplingParams(BaseModel):
    max_completion_tokens: Optional[int] = None
   # old  max_completion_tokens: int
    """The maximum number of tokens in the generated output."""

    seed: Optional[int] = None
   # old  seed: int
    """A seed value to initialize the randomness, during sampling."""

    temperature: Optional[float] = None
   # old  temperature: float
    """A higher temperature increases randomness in the outputs."""

    top_p: Optional[float] = None
   # old  top_p: float
    """An alternative to temperature for nucleus sampling; 1.0 includes all tokens."""


class DataSourceCreateEvalResponsesRunDataSource(BaseModel):
    source: Optional[DataSourceCreateEvalResponsesRunDataSourceSource] = None
   # old  source: Required[DataSourceCreateEvalResponsesRunDataSourceSource]
    """A EvalResponsesSource object describing a run data source configuration."""

    type: Optional[Literal["completions"]] = None
   # old  type: Required[Literal["completions"]]
    """The type of run data source. Always `completions`."""

    input_messages: Optional[DataSourceCreateEvalResponsesRunDataSourceInputMessages] = None
   # old  input_messages: DataSourceCreateEvalResponsesRunDataSourceInputMessages

    model: Optional[str] = None
   # old  model: str
    """The name of the model to use for generating completions (e.g. "o3-mini")."""

    sampling_params: Optional[DataSourceCreateEvalResponsesRunDataSourceSamplingParams] = None
   # old  sampling_params: DataSourceCreateEvalResponsesRunDataSourceSamplingParams


DataSource = Union[
    CreateEvalJSONLRunDataSourceParam,
    CreateEvalCompletionsRunDataSourceParam,
    DataSourceCreateEvalResponsesRunDataSource,
]












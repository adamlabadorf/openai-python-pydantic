# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from pydantic import BaseModel, Field
from typing import List, Optional

from typing import Dict,Union,List,Optional
from typing_extensions import Literal

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
    data_source: "DataSource"= None
    
    """Details about the run's data source."""

    metadata: "Optional[Metadata]"= None
    
    """Set of 16 key-value pairs that can be attached to an object.

    This can be useful for storing additional information about the object in a
    structured format, and querying for objects via API or the dashboard.

    Keys are strings with a maximum length of 64 characters. Values are strings with
    a maximum length of 512 characters.
    """

    name: "Optional[str]"= None
    
    """The name of the run."""


class DataSourceCreateEvalResponsesRunDataSourceSourceFileContentContent(BaseModel):
    item: "Dict[str, object]"= None
    

    sample: "Optional[Dict[str, object]]"= None
    


class DataSourceCreateEvalResponsesRunDataSourceSourceFileContent(BaseModel):
    content: "List[DataSourceCreateEvalResponsesRunDataSourceSourceFileContentContent]"= None
    
    """The content of the jsonl file."""

    type: "Literal['file_content']"= None
    
    """The type of jsonl source. Always `file_content`."""


class DataSourceCreateEvalResponsesRunDataSourceSourceFileID(BaseModel):
    id: "str"= None
    
    """The identifier of the file."""

    type: "Literal['file_id']"= None
    
    """The type of jsonl source. Always `file_id`."""


class DataSourceCreateEvalResponsesRunDataSourceSourceResponses(BaseModel):
    type: "Literal['responses']"= None
    
    """The type of run data source. Always `responses`."""

    allow_parallel_tool_calls: "Optional[bool]"= None
    
    """Whether to allow parallel tool calls.

    This is a query parameter used to select responses.
    """

    created_after: "Optional[int]"= None
    
    """Only include items created after this timestamp (inclusive).

    This is a query parameter used to select responses.
    """

    created_before: "Optional[int]"= None
    
    """Only include items created before this timestamp (inclusive).

    This is a query parameter used to select responses.
    """

    has_tool_calls: "Optional[bool]"= None
    
    """Whether the response has tool calls.

    This is a query parameter used to select responses.
    """

    instructions_search: "Optional[str]"= None
    
    """Optional search string for instructions.

    This is a query parameter used to select responses.
    """

    metadata: "Optional[object]"= None
    
    """Metadata filter for the responses.

    This is a query parameter used to select responses.
    """

    model: "Optional[str]"= None
    
    """The name of the model to find responses for.

    This is a query parameter used to select responses.
    """

    reasoning_effort: "Optional[ReasoningEffort]"= None
    
    """Optional reasoning effort parameter.

    This is a query parameter used to select responses.
    """

    temperature: "Optional[float]"= None
    
    """Sampling temperature. This is a query parameter used to select responses."""

    top_p: "Optional[float]"= None
    
    """Nucleus sampling parameter. This is a query parameter used to select responses."""

    users: "Optional[List[str]]"= None
    
    """List of user identifiers. This is a query parameter used to select responses."""


DataSourceCreateEvalResponsesRunDataSourceSource = Union[
    DataSourceCreateEvalResponsesRunDataSourceSourceFileContent,
    DataSourceCreateEvalResponsesRunDataSourceSourceFileID,
    DataSourceCreateEvalResponsesRunDataSourceSourceResponses,
]


class DataSourceCreateEvalResponsesRunDataSourceInputMessagesTemplateTemplateChatMessage(BaseModel):
    content: "str"= None
    
    """The content of the message."""

    role: "str"= None
    
    """The role of the message (e.g. "system", "assistant", "user")."""


class DataSourceCreateEvalResponsesRunDataSourceInputMessagesTemplateTemplateEvalItemContentOutputText(
    BaseModel
):
    text: "str"= None
    
    """The text output from the model."""

    type: "Literal['output_text']"= None
    
    """The type of the output text. Always `output_text`."""


DataSourceCreateEvalResponsesRunDataSourceInputMessagesTemplateTemplateEvalItemContent = Union[
    str,
    ResponseInputTextParam,
    DataSourceCreateEvalResponsesRunDataSourceInputMessagesTemplateTemplateEvalItemContentOutputText,
]


class DataSourceCreateEvalResponsesRunDataSourceInputMessagesTemplateTemplateEvalItem(BaseModel):
    content: "DataSourceCreateEvalResponsesRunDataSourceInputMessagesTemplateTemplateEvalItemContent"= None
    
    """Text inputs to the model - can contain template strings."""

    role: "Literal['user', 'assistant', 'system', 'developer']"= None
    
    """The role of the message input.

    One of `user`, `assistant`, `system`, or `developer`.
    """

    type: "Optional[Literal['message']]"= None
    
    """The type of the message input. Always `message`."""


DataSourceCreateEvalResponsesRunDataSourceInputMessagesTemplateTemplate = Union[
    DataSourceCreateEvalResponsesRunDataSourceInputMessagesTemplateTemplateChatMessage,
    DataSourceCreateEvalResponsesRunDataSourceInputMessagesTemplateTemplateEvalItem,
]


class DataSourceCreateEvalResponsesRunDataSourceInputMessagesTemplate(BaseModel):
    template: "List[DataSourceCreateEvalResponsesRunDataSourceInputMessagesTemplateTemplate]"= None
    
    """A list of chat messages forming the prompt or context.

    May include variable references to the "item" namespace, ie {{item.name}}.
    """

    type: "Literal['template']"= None
    
    """The type of input messages. Always `template`."""


class DataSourceCreateEvalResponsesRunDataSourceInputMessagesItemReference(BaseModel):
    item_reference: "str"= None
    
    """A reference to a variable in the "item" namespace. Ie, "item.name" """

    type: "Literal['item_reference']"= None
    
    """The type of input messages. Always `item_reference`."""


DataSourceCreateEvalResponsesRunDataSourceInputMessages = Union[
    DataSourceCreateEvalResponsesRunDataSourceInputMessagesTemplate,
    DataSourceCreateEvalResponsesRunDataSourceInputMessagesItemReference,
]


class DataSourceCreateEvalResponsesRunDataSourceSamplingParams(BaseModel):
    max_completion_tokens: "Optional[int]"= None
    
    """The maximum number of tokens in the generated output."""

    seed: "Optional[int]"= None
    
    """A seed value to initialize the randomness, during sampling."""

    temperature: "Optional[float]"= None
    
    """A higher temperature increases randomness in the outputs."""

    top_p: "Optional[float]"= None
    
    """An alternative to temperature for nucleus sampling; 1.0 includes all tokens."""


class DataSourceCreateEvalResponsesRunDataSource(BaseModel):
    source: "DataSourceCreateEvalResponsesRunDataSourceSource"= None
    
    """A EvalResponsesSource object describing a run data source configuration."""

    type: "Literal['completions']"= None
    
    """The type of run data source. Always `completions`."""

    input_messages: "Optional[DataSourceCreateEvalResponsesRunDataSourceInputMessages]"= None
    

    model: "Optional[str]"= None
    
    """The name of the model to use for generating completions (e.g. "o3-mini")."""

    sampling_params: "Optional[DataSourceCreateEvalResponsesRunDataSourceSamplingParams]"= None
    


DataSource = Union[
    CreateEvalJSONLRunDataSourceParam,
    CreateEvalCompletionsRunDataSourceParam,
    DataSourceCreateEvalResponsesRunDataSource,
]
RunCreateParams.model_rebuild()
DataSourceCreateEvalResponsesRunDataSourceSourceFileContentContent.model_rebuild()
DataSourceCreateEvalResponsesRunDataSourceSourceFileContent.model_rebuild()
DataSourceCreateEvalResponsesRunDataSourceSourceFileID.model_rebuild()
DataSourceCreateEvalResponsesRunDataSourceSourceResponses.model_rebuild()
DataSourceCreateEvalResponsesRunDataSourceInputMessagesTemplateTemplateChatMessage.model_rebuild()
DataSourceCreateEvalResponsesRunDataSourceInputMessagesTemplateTemplateEvalItemContentOutputText.model_rebuild()
DataSourceCreateEvalResponsesRunDataSourceInputMessagesTemplateTemplateEvalItem.model_rebuild()
DataSourceCreateEvalResponsesRunDataSourceInputMessagesTemplate.model_rebuild()
DataSourceCreateEvalResponsesRunDataSourceInputMessagesItemReference.model_rebuild()
DataSourceCreateEvalResponsesRunDataSourceSamplingParams.model_rebuild()
DataSourceCreateEvalResponsesRunDataSource.model_rebuild()


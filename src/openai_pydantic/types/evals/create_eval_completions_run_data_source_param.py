# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from pydantic import BaseModel, Field
from typing import List, Optional

from typing import Union,Dict,Optional
from typing_extensions import Literal

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
    item: "Dict[str, object]"
    

    sample: "Optional[Dict[str, object]]"= None
    


class SourceFileContent(BaseModel):
    content: "List[SourceFileContentContent]"
    
    """The content of the jsonl file."""

    type: "Literal['file_content']"
    
    """The type of jsonl source. Always `file_content`."""


class SourceFileID(BaseModel):
    id: "str"
    
    """The identifier of the file."""

    type: "Literal['file_id']"
    
    """The type of jsonl source. Always `file_id`."""


class SourceStoredCompletions(BaseModel):
    type: "Literal['stored_completions']"
    
    """The type of source. Always `stored_completions`."""

    created_after: "Optional[int]"= None
    
    """An optional Unix timestamp to filter items created after this time."""

    created_before: "Optional[int]"= None
    
    """An optional Unix timestamp to filter items created before this time."""

    limit: "Optional[int]"= None
    
    """An optional maximum number of items to return."""

    metadata: "Optional[Metadata]"= None
    
    """Set of 16 key-value pairs that can be attached to an object.

    This can be useful for storing additional information about the object in a
    structured format, and querying for objects via API or the dashboard.

    Keys are strings with a maximum length of 64 characters. Values are strings with
    a maximum length of 512 characters.
    """

    model: "Optional[str]"= None
    
    """An optional model to filter by (e.g., 'gpt-4o')."""


Source = Union[SourceFileContent, SourceFileID, SourceStoredCompletions]


class InputMessagesTemplateTemplateMessageContentOutputText(BaseModel):
    text: "str"
    
    """The text output from the model."""

    type: "Literal['output_text']"
    
    """The type of the output text. Always `output_text`."""


InputMessagesTemplateTemplateMessageContent = Union[
    str, ResponseInputTextParam, InputMessagesTemplateTemplateMessageContentOutputText
]


class InputMessagesTemplateTemplateMessage(BaseModel):
    content: "InputMessagesTemplateTemplateMessageContent"
    
    """Text inputs to the model - can contain template strings."""

    role: "Literal['user', 'assistant', 'system', 'developer']"
    
    """The role of the message input.

    One of `user`, `assistant`, `system`, or `developer`.
    """

    type: "Optional[Literal['message']]"= None
    
    """The type of the message input. Always `message`."""


InputMessagesTemplateTemplate = Union[EasyInputMessageParam, InputMessagesTemplateTemplateMessage]


class InputMessagesTemplate(BaseModel):
    template: "List[InputMessagesTemplateTemplate]"
    
    """A list of chat messages forming the prompt or context.

    May include variable references to the "item" namespace, ie {{item.name}}.
    """

    type: "Literal['template']"
    
    """The type of input messages. Always `template`."""


class InputMessagesItemReference(BaseModel):
    item_reference: "str"
    
    """A reference to a variable in the "item" namespace. Ie, "item.name" """

    type: "Literal['item_reference']"
    
    """The type of input messages. Always `item_reference`."""


InputMessages = Union[InputMessagesTemplate, InputMessagesItemReference]


class SamplingParams(BaseModel):
    max_completion_tokens: "Optional[int]"= None
    
    """The maximum number of tokens in the generated output."""

    seed: "Optional[int]"= None
    
    """A seed value to initialize the randomness, during sampling."""

    temperature: "Optional[float]"= None
    
    """A higher temperature increases randomness in the outputs."""

    top_p: "Optional[float]"= None
    
    """An alternative to temperature for nucleus sampling; 1.0 includes all tokens."""


class CreateEvalCompletionsRunDataSourceParam(BaseModel):
    source: "Source"
    
    """A StoredCompletionsRunDataSource configuration describing a set of filters"""

    type: "Literal['completions']"
    
    """The type of run data source. Always `completions`."""

    input_messages: "Optional[InputMessages]"= None
    

    model: "Optional[str]"= None
    
    """The name of the model to use for generating completions (e.g. "o3-mini")."""

    sampling_params: "Optional[SamplingParams]"= None
    
SourceFileContentContent.model_rebuild()
SourceFileContent.model_rebuild()
SourceFileID.model_rebuild()
SourceStoredCompletions.model_rebuild()
InputMessagesTemplateTemplateMessageContentOutputText.model_rebuild()
InputMessagesTemplateTemplateMessage.model_rebuild()
InputMessagesTemplate.model_rebuild()
InputMessagesItemReference.model_rebuild()
SamplingParams.model_rebuild()
CreateEvalCompletionsRunDataSourceParam.model_rebuild()


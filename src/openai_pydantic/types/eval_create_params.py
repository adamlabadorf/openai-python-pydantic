# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from pydantic import BaseModel, Field
from typing import List, Optional

from typing import Union,Optional,Dict,List
from typing_extensions import Literal

from .shared_params.metadata import Metadata
from .eval_string_check_grader_param import EvalStringCheckGraderParam
from .eval_text_similarity_grader_param import EvalTextSimilarityGraderParam
from .responses.response_input_text_param import ResponseInputTextParam

__all__ = [
    "EvalCreateParams",
    "DataSourceConfig",
    "DataSourceConfigCustom",
    "DataSourceConfigLogs",
    "TestingCriterion",
    "TestingCriterionLabelModel",
    "TestingCriterionLabelModelInput",
    "TestingCriterionLabelModelInputSimpleInputMessage",
    "TestingCriterionLabelModelInputEvalItem",
    "TestingCriterionLabelModelInputEvalItemContent",
    "TestingCriterionLabelModelInputEvalItemContentOutputText",
    "TestingCriterionPython",
    "TestingCriterionScoreModel",
    "TestingCriterionScoreModelInput",
    "TestingCriterionScoreModelInputContent",
    "TestingCriterionScoreModelInputContentOutputText",
]


class EvalCreateParams(BaseModel):
    data_source_config: "DataSourceConfig"
    
    """The configuration for the data source used for the evaluation runs."""

    testing_criteria: "List[TestingCriterion]"
    
    """A list of graders for all eval runs in this group."""

    metadata: "Optional[Metadata]"= None
    
    """Set of 16 key-value pairs that can be attached to an object.

    This can be useful for storing additional information about the object in a
    structured format, and querying for objects via API or the dashboard.

    Keys are strings with a maximum length of 64 characters. Values are strings with
    a maximum length of 512 characters.
    """

    name: "Optional[str]"= None
    
    """The name of the evaluation."""


class DataSourceConfigCustom(BaseModel):
    item_schema: "Dict[str, object]"
    
    """The json schema for each row in the data source."""

    type: "Literal['custom']"
    
    """The type of data source. Always `custom`."""

    include_sample_schema: "Optional[bool]"= None
    
    """
    Whether the eval should expect you to populate the sample namespace (ie, by
    generating responses off of your data source)
    """


class DataSourceConfigLogs(BaseModel):
    type: "Literal['logs']"
    
    """The type of data source. Always `logs`."""

    metadata: "Optional[Dict[str, object]]"= None
    
    """Metadata filters for the logs data source."""


DataSourceConfig = Union[DataSourceConfigCustom, DataSourceConfigLogs]


class TestingCriterionLabelModelInputSimpleInputMessage(BaseModel):
    content: "str"
    
    """The content of the message."""

    role: "str"
    
    """The role of the message (e.g. "system", "assistant", "user")."""


class TestingCriterionLabelModelInputEvalItemContentOutputText(BaseModel):
    text: "str"
    
    """The text output from the model."""

    type: "Literal['output_text']"
    
    """The type of the output text. Always `output_text`."""


TestingCriterionLabelModelInputEvalItemContent = Union[
    str, ResponseInputTextParam, TestingCriterionLabelModelInputEvalItemContentOutputText
]


class TestingCriterionLabelModelInputEvalItem(BaseModel):
    content: "TestingCriterionLabelModelInputEvalItemContent"
    
    """Text inputs to the model - can contain template strings."""

    role: "Literal['user', 'assistant', 'system', 'developer']"
    
    """The role of the message input.

    One of `user`, `assistant`, `system`, or `developer`.
    """

    type: "Optional[Literal['message']]"= None
    
    """The type of the message input. Always `message`."""


TestingCriterionLabelModelInput = Union[
    TestingCriterionLabelModelInputSimpleInputMessage, TestingCriterionLabelModelInputEvalItem
]


class TestingCriterionLabelModel(BaseModel):
    input: "List[TestingCriterionLabelModelInput]"
    
    """A list of chat messages forming the prompt or context.

    May include variable references to the "item" namespace, ie {{item.name}}.
    """

    labels: "List[str]"
    
    """The labels to classify to each item in the evaluation."""

    model: "str"
    
    """The model to use for the evaluation. Must support structured outputs."""

    name: "str"
    
    """The name of the grader."""

    passing_labels: "List[str]"
    
    """The labels that indicate a passing result. Must be a subset of labels."""

    type: "Literal['label_model']"
    
    """The object type, which is always `label_model`."""


class TestingCriterionPython(BaseModel):
    name: "str"
    
    """The name of the grader."""

    source: "str"
    
    """The source code of the python script."""

    type: "Literal['python']"
    
    """The object type, which is always `python`."""

    image_tag: "Optional[str]"= None
    
    """The image tag to use for the python script."""

    pass_threshold: "Optional[float]"= None
    
    """The threshold for the score."""


class TestingCriterionScoreModelInputContentOutputText(BaseModel):
    text: "str"
    
    """The text output from the model."""

    type: "Literal['output_text']"
    
    """The type of the output text. Always `output_text`."""


TestingCriterionScoreModelInputContent = Union[
    str, ResponseInputTextParam, TestingCriterionScoreModelInputContentOutputText
]


class TestingCriterionScoreModelInput(BaseModel):
    content: "TestingCriterionScoreModelInputContent"
    
    """Text inputs to the model - can contain template strings."""

    role: "Literal['user', 'assistant', 'system', 'developer']"
    
    """The role of the message input.

    One of `user`, `assistant`, `system`, or `developer`.
    """

    type: "Optional[Literal['message']]"= None
    
    """The type of the message input. Always `message`."""


class TestingCriterionScoreModel(BaseModel):
    input: "List[TestingCriterionScoreModelInput]"
    
    """The input text. This may include template strings."""

    model: "str"
    
    """The model to use for the evaluation."""

    name: "str"
    
    """The name of the grader."""

    type: "Literal['score_model']"
    
    """The object type, which is always `score_model`."""

    pass_threshold: "Optional[float]"= None
    
    """The threshold for the score."""

    range: "Optional[List[float]]"=Field(default_factory=list)
    
    """The range of the score. Defaults to `[0, 1]`."""

    sampling_params: "Optional[object]"= None
    
    """The sampling parameters for the model."""


TestingCriterion = Union[
    TestingCriterionLabelModel,
    EvalStringCheckGraderParam,
    EvalTextSimilarityGraderParam,
    TestingCriterionPython,
    TestingCriterionScoreModel,
]
EvalCreateParams.model_rebuild()
DataSourceConfigCustom.model_rebuild()
DataSourceConfigLogs.model_rebuild()
TestingCriterionLabelModelInputSimpleInputMessage.model_rebuild()
TestingCriterionLabelModelInputEvalItemContentOutputText.model_rebuild()
TestingCriterionLabelModelInputEvalItem.model_rebuild()
TestingCriterionLabelModel.model_rebuild()
TestingCriterionPython.model_rebuild()
TestingCriterionScoreModelInputContentOutputText.model_rebuild()
TestingCriterionScoreModelInput.model_rebuild()
TestingCriterionScoreModel.model_rebuild()


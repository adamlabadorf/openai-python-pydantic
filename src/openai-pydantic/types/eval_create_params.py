# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List, Union, Iterable, Optional
from typing_extensions import Literal
from pydantic import BaseModel
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
    data_source_config: Optional[DataSourceConfig] = None
    # old  data_source_config: Optional[DataSourceConfig] = None
    # old  data_source_config: Optional[DataSourceConfig] = None
    # old  data_source_config: Optional[DataSourceConfig] = None
    # old  data_source_config: Optional[DataSourceConfig] = None
    # old  data_source_config: Optional[DataSourceConfig] = None
    # old  data_source_config: Optional[DataSourceConfig] = None
    # old  data_source_config: Optional[DataSourceConfig] = None
    # old  data_source_config: Optional[DataSourceConfig] = None
    # old  data_source_config: Optional[DataSourceConfig] = None
    # old  data_source_config: DataSourceConfig = None
    # old  data_source_config: Required[DataSourceConfig]
    """The configuration for the data source used for the evaluation runs."""

    testing_criteria: Optional[List[TestingCriterion]] = None
    # old  testing_criteria: Optional[List[TestingCriterion]] = None
    # old  testing_criteria: Optional[List[TestingCriterion]] = None
    # old  testing_criteria: Optional[List[TestingCriterion]] = None
    # old  testing_criteria: Optional[List[TestingCriterion]] = None
    # old  testing_criteria: Optional[List[TestingCriterion]] = None
    # old  testing_criteria: Optional[List[TestingCriterion]] = None
    # old  testing_criteria: Optional[List[TestingCriterion]] = None
    # old  testing_criteria: Optional[List[TestingCriterion]] = None
    # old  testing_criteria: Optional[List[TestingCriterion]] = None
    # old  testing_criteria: List[TestingCriterion] = None
    # old  testing_criteria: Required[Iterable[TestingCriterion]]
    """A list of graders for all eval runs in this group."""

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

    name: Optional[str] = None
    # old  name: Optional[str] = None
    # old  name: Optional[str] = None
    # old  name: Optional[str] = None
    # old  name: Optional[str] = None
    # old  name: Optional[str] = None
    # old  name: Optional[str] = None
    # old  name: Optional[str] = None
    # old  name: Optional[str] = None
    # old  name: Optional[str] = None
    # old  name: Optional[str] = None
    # old  name: str
    """The name of the evaluation."""


class DataSourceConfigCustom(BaseModel):
    item_schema: Optional[Dict[str, object]] = None
    # old  item_schema: Optional[Dict[str, object]] = None
    # old  item_schema: Optional[Dict[str, object]] = None
    # old  item_schema: Optional[Dict[str, object]] = None
    # old  item_schema: Optional[Dict[str, object]] = None
    # old  item_schema: Optional[Dict[str, object]] = None
    # old  item_schema: Optional[Dict[str, object]] = None
    # old  item_schema: Optional[Dict[str, object]] = None
    # old  item_schema: Optional[Dict[str, object]] = None
    # old  item_schema: Optional[Dict[str, object]] = None
    # old  item_schema: Dict[str, object] = None
    # old  item_schema: Required[Dict[str, object]]
    """The json schema for each row in the data source."""

    type: Optional[Literal["custom"]] = None
    # old  type: Optional[Literal["custom"]] = None
    # old  type: Optional[Literal["custom"]] = None
    # old  type: Optional[Literal["custom"]] = None
    # old  type: Optional[Literal["custom"]] = None
    # old  type: Optional[Literal["custom"]] = None
    # old  type: Optional[Literal["custom"]] = None
    # old  type: Optional[Literal["custom"]] = None
    # old  type: Optional[Literal["custom"]] = None
    # old  type: Optional[Literal["custom"]] = None
    # old  type: Literal["custom"] = None
    # old  type: Required[Literal["custom"]]
    """The type of data source. Always `custom`."""

    include_sample_schema: Optional[bool] = None
    # old  include_sample_schema: Optional[bool] = None
    # old  include_sample_schema: Optional[bool] = None
    # old  include_sample_schema: Optional[bool] = None
    # old  include_sample_schema: Optional[bool] = None
    # old  include_sample_schema: Optional[bool] = None
    # old  include_sample_schema: Optional[bool] = None
    # old  include_sample_schema: Optional[bool] = None
    # old  include_sample_schema: Optional[bool] = None
    # old  include_sample_schema: Optional[bool] = None
    # old  include_sample_schema: Optional[bool] = None
    # old  include_sample_schema: bool
    """
    Whether the eval should expect you to populate the sample namespace (ie, by
    generating responses off of your data source)
    """


class DataSourceConfigLogs(BaseModel):
    type: Optional[Literal["logs"]] = None
    # old  type: Optional[Literal["logs"]] = None
    # old  type: Optional[Literal["logs"]] = None
    # old  type: Optional[Literal["logs"]] = None
    # old  type: Optional[Literal["logs"]] = None
    # old  type: Optional[Literal["logs"]] = None
    # old  type: Optional[Literal["logs"]] = None
    # old  type: Optional[Literal["logs"]] = None
    # old  type: Optional[Literal["logs"]] = None
    # old  type: Optional[Literal["logs"]] = None
    # old  type: Literal["logs"] = None
    # old  type: Required[Literal["logs"]]
    """The type of data source. Always `logs`."""

    metadata: Optional[Dict[str, object]] = None
    # old  metadata: Optional[Dict[str, object]] = None
    # old  metadata: Optional[Dict[str, object]] = None
    # old  metadata: Optional[Dict[str, object]] = None
    # old  metadata: Optional[Dict[str, object]] = None
    # old  metadata: Optional[Dict[str, object]] = None
    # old  metadata: Optional[Dict[str, object]] = None
    # old  metadata: Optional[Dict[str, object]] = None
    # old  metadata: Optional[Dict[str, object]] = None
    # old  metadata: Optional[Dict[str, object]] = None
    # old  metadata: Optional[Dict[str, object]] = None
    # old  metadata: Dict[str, object]
    """Metadata filters for the logs data source."""


DataSourceConfig = Union[DataSourceConfigCustom, DataSourceConfigLogs] # old DataSourceConfig: TypeAlias = Union[DataSourceConfigCustom, DataSourceConfigLogs]


class TestingCriterionLabelModelInputSimpleInputMessage(BaseModel):
    content: Optional[str] = None
    # old  content: Optional[str] = None
    # old  content: Optional[str] = None
    # old  content: Optional[str] = None
    # old  content: Optional[str] = None
    # old  content: Optional[str] = None
    # old  content: Optional[str] = None
    # old  content: Optional[str] = None
    # old  content: Optional[str] = None
    # old  content: Optional[str] = None
    # old  content: str = None
    # old  content: Required[str]
    """The content of the message."""

    role: Optional[str] = None
    # old  role: Optional[str] = None
    # old  role: Optional[str] = None
    # old  role: Optional[str] = None
    # old  role: Optional[str] = None
    # old  role: Optional[str] = None
    # old  role: Optional[str] = None
    # old  role: Optional[str] = None
    # old  role: Optional[str] = None
    # old  role: Optional[str] = None
    # old  role: str = None
    # old  role: Required[str]
    """The role of the message (e.g. "system", "assistant", "user")."""


class TestingCriterionLabelModelInputEvalItemContentOutputText(BaseModel):
    text: Optional[str] = None
    # old  text: Optional[str] = None
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
    # old  type: Optional[Literal["output_text"]] = None
    # old  type: Literal["output_text"] = None
    # old  type: Required[Literal["output_text"]]
    """The type of the output text. Always `output_text`."""


TestingCriterionLabelModelInputEvalItemContent = Union[ # old TestingCriterionLabelModelInputEvalItemContent: TypeAlias = Union[
    str, ResponseInputTextParam, TestingCriterionLabelModelInputEvalItemContentOutputText
]


class TestingCriterionLabelModelInputEvalItem(BaseModel):
    content: Optional[TestingCriterionLabelModelInputEvalItemContent] = None
    # old  content: Optional[TestingCriterionLabelModelInputEvalItemContent] = None
    # old  content: Optional[TestingCriterionLabelModelInputEvalItemContent] = None
    # old  content: Optional[TestingCriterionLabelModelInputEvalItemContent] = None
    # old  content: Optional[TestingCriterionLabelModelInputEvalItemContent] = None
    # old  content: Optional[TestingCriterionLabelModelInputEvalItemContent] = None
    # old  content: Optional[TestingCriterionLabelModelInputEvalItemContent] = None
    # old  content: Optional[TestingCriterionLabelModelInputEvalItemContent] = None
    # old  content: Optional[TestingCriterionLabelModelInputEvalItemContent] = None
    # old  content: Optional[TestingCriterionLabelModelInputEvalItemContent] = None
    # old  content: TestingCriterionLabelModelInputEvalItemContent = None
    # old  content: Required[TestingCriterionLabelModelInputEvalItemContent]
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
    # old  type: Optional[Literal["message"]] = None
    # old  type: Literal["message"]
    """The type of the message input. Always `message`."""


TestingCriterionLabelModelInput = Union[ # old TestingCriterionLabelModelInput: TypeAlias = Union[
    TestingCriterionLabelModelInputSimpleInputMessage, TestingCriterionLabelModelInputEvalItem
]


class TestingCriterionLabelModel(BaseModel):
    input: Optional[List[TestingCriterionLabelModelInput]] = None
    # old  input: Optional[List[TestingCriterionLabelModelInput]] = None
    # old  input: Optional[List[TestingCriterionLabelModelInput]] = None
    # old  input: Optional[List[TestingCriterionLabelModelInput]] = None
    # old  input: Optional[List[TestingCriterionLabelModelInput]] = None
    # old  input: Optional[List[TestingCriterionLabelModelInput]] = None
    # old  input: Optional[List[TestingCriterionLabelModelInput]] = None
    # old  input: Optional[List[TestingCriterionLabelModelInput]] = None
    # old  input: Optional[List[TestingCriterionLabelModelInput]] = None
    # old  input: Optional[List[TestingCriterionLabelModelInput]] = None
    # old  input: List[TestingCriterionLabelModelInput] = None
    # old  input: Required[Iterable[TestingCriterionLabelModelInput]]
    """A list of chat messages forming the prompt or context.

    May include variable references to the "item" namespace, ie {{item.name}}.
    """

    labels: Optional[List[str]] = None
    # old  labels: Optional[List[str]] = None
    # old  labels: Optional[List[str]] = None
    # old  labels: Optional[List[str]] = None
    # old  labels: Optional[List[str]] = None
    # old  labels: Optional[List[str]] = None
    # old  labels: Optional[List[str]] = None
    # old  labels: Optional[List[str]] = None
    # old  labels: Optional[List[str]] = None
    # old  labels: Optional[List[str]] = None
    # old  labels: List[str] = None
    # old  labels: Required[List[str]]
    """The labels to classify to each item in the evaluation."""

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
    # old  model: str = None
    # old  model: Required[str]
    """The model to use for the evaluation. Must support structured outputs."""

    name: Optional[str] = None
    # old  name: Optional[str] = None
    # old  name: Optional[str] = None
    # old  name: Optional[str] = None
    # old  name: Optional[str] = None
    # old  name: Optional[str] = None
    # old  name: Optional[str] = None
    # old  name: Optional[str] = None
    # old  name: Optional[str] = None
    # old  name: Optional[str] = None
    # old  name: str = None
    # old  name: Required[str]
    """The name of the grader."""

    passing_labels: Optional[List[str]] = None
    # old  passing_labels: Optional[List[str]] = None
    # old  passing_labels: Optional[List[str]] = None
    # old  passing_labels: Optional[List[str]] = None
    # old  passing_labels: Optional[List[str]] = None
    # old  passing_labels: Optional[List[str]] = None
    # old  passing_labels: Optional[List[str]] = None
    # old  passing_labels: Optional[List[str]] = None
    # old  passing_labels: Optional[List[str]] = None
    # old  passing_labels: Optional[List[str]] = None
    # old  passing_labels: List[str] = None
    # old  passing_labels: Required[List[str]]
    """The labels that indicate a passing result. Must be a subset of labels."""

    type: Optional[Literal["label_model"]] = None
    # old  type: Optional[Literal["label_model"]] = None
    # old  type: Optional[Literal["label_model"]] = None
    # old  type: Optional[Literal["label_model"]] = None
    # old  type: Optional[Literal["label_model"]] = None
    # old  type: Optional[Literal["label_model"]] = None
    # old  type: Optional[Literal["label_model"]] = None
    # old  type: Optional[Literal["label_model"]] = None
    # old  type: Optional[Literal["label_model"]] = None
    # old  type: Optional[Literal["label_model"]] = None
    # old  type: Literal["label_model"] = None
    # old  type: Required[Literal["label_model"]]
    """The object type, which is always `label_model`."""


class TestingCriterionPython(BaseModel):
    name: Optional[str] = None
    # old  name: Optional[str] = None
    # old  name: Optional[str] = None
    # old  name: Optional[str] = None
    # old  name: Optional[str] = None
    # old  name: Optional[str] = None
    # old  name: Optional[str] = None
    # old  name: Optional[str] = None
    # old  name: Optional[str] = None
    # old  name: Optional[str] = None
    # old  name: str = None
    # old  name: Required[str]
    """The name of the grader."""

    source: Optional[str] = None
    # old  source: Optional[str] = None
    # old  source: Optional[str] = None
    # old  source: Optional[str] = None
    # old  source: Optional[str] = None
    # old  source: Optional[str] = None
    # old  source: Optional[str] = None
    # old  source: Optional[str] = None
    # old  source: Optional[str] = None
    # old  source: Optional[str] = None
    # old  source: str = None
    # old  source: Required[str]
    """The source code of the python script."""

    type: Optional[Literal["python"]] = None
    # old  type: Optional[Literal["python"]] = None
    # old  type: Optional[Literal["python"]] = None
    # old  type: Optional[Literal["python"]] = None
    # old  type: Optional[Literal["python"]] = None
    # old  type: Optional[Literal["python"]] = None
    # old  type: Optional[Literal["python"]] = None
    # old  type: Optional[Literal["python"]] = None
    # old  type: Optional[Literal["python"]] = None
    # old  type: Optional[Literal["python"]] = None
    # old  type: Literal["python"] = None
    # old  type: Required[Literal["python"]]
    """The object type, which is always `python`."""

    image_tag: Optional[str] = None
    # old  image_tag: Optional[str] = None
    # old  image_tag: Optional[str] = None
    # old  image_tag: Optional[str] = None
    # old  image_tag: Optional[str] = None
    # old  image_tag: Optional[str] = None
    # old  image_tag: Optional[str] = None
    # old  image_tag: Optional[str] = None
    # old  image_tag: Optional[str] = None
    # old  image_tag: Optional[str] = None
    # old  image_tag: Optional[str] = None
    # old  image_tag: str
    """The image tag to use for the python script."""

    pass_threshold: Optional[float] = None
    # old  pass_threshold: Optional[float] = None
    # old  pass_threshold: Optional[float] = None
    # old  pass_threshold: Optional[float] = None
    # old  pass_threshold: Optional[float] = None
    # old  pass_threshold: Optional[float] = None
    # old  pass_threshold: Optional[float] = None
    # old  pass_threshold: Optional[float] = None
    # old  pass_threshold: Optional[float] = None
    # old  pass_threshold: Optional[float] = None
    # old  pass_threshold: Optional[float] = None
    # old  pass_threshold: float
    """The threshold for the score."""


class TestingCriterionScoreModelInputContentOutputText(BaseModel):
    text: Optional[str] = None
    # old  text: Optional[str] = None
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
    # old  type: Optional[Literal["output_text"]] = None
    # old  type: Literal["output_text"] = None
    # old  type: Required[Literal["output_text"]]
    """The type of the output text. Always `output_text`."""


TestingCriterionScoreModelInputContent = Union[ # old TestingCriterionScoreModelInputContent: TypeAlias = Union[
    str, ResponseInputTextParam, TestingCriterionScoreModelInputContentOutputText
]


class TestingCriterionScoreModelInput(BaseModel):
    content: Optional[TestingCriterionScoreModelInputContent] = None
    # old  content: Optional[TestingCriterionScoreModelInputContent] = None
    # old  content: Optional[TestingCriterionScoreModelInputContent] = None
    # old  content: Optional[TestingCriterionScoreModelInputContent] = None
    # old  content: Optional[TestingCriterionScoreModelInputContent] = None
    # old  content: Optional[TestingCriterionScoreModelInputContent] = None
    # old  content: Optional[TestingCriterionScoreModelInputContent] = None
    # old  content: Optional[TestingCriterionScoreModelInputContent] = None
    # old  content: Optional[TestingCriterionScoreModelInputContent] = None
    # old  content: Optional[TestingCriterionScoreModelInputContent] = None
    # old  content: TestingCriterionScoreModelInputContent = None
    # old  content: Required[TestingCriterionScoreModelInputContent]
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
    # old  type: Optional[Literal["message"]] = None
    # old  type: Literal["message"]
    """The type of the message input. Always `message`."""


class TestingCriterionScoreModel(BaseModel):
    input: Optional[List[TestingCriterionScoreModelInput]] = None
    # old  input: Optional[List[TestingCriterionScoreModelInput]] = None
    # old  input: Optional[List[TestingCriterionScoreModelInput]] = None
    # old  input: Optional[List[TestingCriterionScoreModelInput]] = None
    # old  input: Optional[List[TestingCriterionScoreModelInput]] = None
    # old  input: Optional[List[TestingCriterionScoreModelInput]] = None
    # old  input: Optional[List[TestingCriterionScoreModelInput]] = None
    # old  input: Optional[List[TestingCriterionScoreModelInput]] = None
    # old  input: Optional[List[TestingCriterionScoreModelInput]] = None
    # old  input: Optional[List[TestingCriterionScoreModelInput]] = None
    # old  input: List[TestingCriterionScoreModelInput] = None
    # old  input: Required[Iterable[TestingCriterionScoreModelInput]]
    """The input text. This may include template strings."""

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
    # old  model: str = None
    # old  model: Required[str]
    """The model to use for the evaluation."""

    name: Optional[str] = None
    # old  name: Optional[str] = None
    # old  name: Optional[str] = None
    # old  name: Optional[str] = None
    # old  name: Optional[str] = None
    # old  name: Optional[str] = None
    # old  name: Optional[str] = None
    # old  name: Optional[str] = None
    # old  name: Optional[str] = None
    # old  name: Optional[str] = None
    # old  name: str = None
    # old  name: Required[str]
    """The name of the grader."""

    type: Optional[Literal["score_model"]] = None
    # old  type: Optional[Literal["score_model"]] = None
    # old  type: Optional[Literal["score_model"]] = None
    # old  type: Optional[Literal["score_model"]] = None
    # old  type: Optional[Literal["score_model"]] = None
    # old  type: Optional[Literal["score_model"]] = None
    # old  type: Optional[Literal["score_model"]] = None
    # old  type: Optional[Literal["score_model"]] = None
    # old  type: Optional[Literal["score_model"]] = None
    # old  type: Optional[Literal["score_model"]] = None
    # old  type: Literal["score_model"] = None
    # old  type: Required[Literal["score_model"]]
    """The object type, which is always `score_model`."""

    pass_threshold: Optional[float] = None
    # old  pass_threshold: Optional[float] = None
    # old  pass_threshold: Optional[float] = None
    # old  pass_threshold: Optional[float] = None
    # old  pass_threshold: Optional[float] = None
    # old  pass_threshold: Optional[float] = None
    # old  pass_threshold: Optional[float] = None
    # old  pass_threshold: Optional[float] = None
    # old  pass_threshold: Optional[float] = None
    # old  pass_threshold: Optional[float] = None
    # old  pass_threshold: Optional[float] = None
    # old  pass_threshold: float
    """The threshold for the score."""

    range: Optional[List[float]] = None
    # old  range: Optional[List[float]] = None
    # old  range: Optional[List[float]] = None
    # old  range: Optional[List[float]] = None
    # old  range: Optional[List[float]] = None
    # old  range: Optional[List[float]] = None
    # old  range: Optional[List[float]] = None
    # old  range: Optional[List[float]] = None
    # old  range: Optional[List[float]] = None
    # old  range: Optional[List[float]] = None
    # old  range: Optional[List[float]] = None
    # old  range: Iterable[float]
    """The range of the score. Defaults to `[0, 1]`."""

    sampling_params: Optional[object] = None
    # old  sampling_params: Optional[object] = None
    # old  sampling_params: Optional[object] = None
    # old  sampling_params: Optional[object] = None
    # old  sampling_params: Optional[object] = None
    # old  sampling_params: Optional[object] = None
    # old  sampling_params: Optional[object] = None
    # old  sampling_params: Optional[object] = None
    # old  sampling_params: Optional[object] = None
    # old  sampling_params: Optional[object] = None
    # old  sampling_params: Optional[object] = None
    # old  sampling_params: object
    """The sampling parameters for the model."""


TestingCriterion = Union[ # old TestingCriterion: TypeAlias = Union[
    TestingCriterionLabelModel,
    EvalStringCheckGraderParam,
    EvalTextSimilarityGraderParam,
    TestingCriterionPython,
    TestingCriterionScoreModel,
]












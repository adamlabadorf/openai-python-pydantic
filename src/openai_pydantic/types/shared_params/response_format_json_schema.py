# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Optional
from typing_extensions import Literal
from pydantic import BaseModel
__all__ = ["ResponseFormatJSONSchema", "JSONSchema"]


class JSONSchema(BaseModel):
    name: Optional[str] = None
    # old  name: str = None
    # old  name: Required[str]
    """The name of the response format.

    Must be a-z, A-Z, 0-9, or contain underscores and dashes, with a maximum length
    of 64.
    """

    description: Optional[str] = None
    # old  description: Optional[str] = None
    # old  description: str
    """
    A description of what the response format is for, used by the model to determine
    how to respond in the format.
    """

    schema: Optional[Dict[str, object]] = None
    # old  schema: Optional[Dict[str, object]] = None
    # old  schema: Dict[str, object]
    """
    The schema for the response format, described as a JSON Schema object. Learn how
    to build JSON schemas [here](https://json-schema.org/).
    """

    strict: Optional[bool] = None
    # old  strict: Optional[bool] = None
    # old  strict: Optional[bool]
    """
    Whether to enable strict schema adherence when generating the output. If set to
    true, the model will always follow the exact schema defined in the `schema`
    field. Only a subset of JSON Schema is supported when `strict` is `true`. To
    learn more, read the
    [Structured Outputs guide](https://platform.openai.com/docs/guides/structured-outputs).
    """


class ResponseFormatJSONSchema(BaseModel):
    json_schema: Optional[JSONSchema] = None
    # old  json_schema: JSONSchema = None
    # old  json_schema: Required[JSONSchema]
    """Structured Outputs configuration options, including a JSON Schema."""

    type: Optional[Literal["json_schema"]] = None
    # old  type: Literal["json_schema"] = None
    # old  type: Required[Literal["json_schema"]]
    """The type of response format being defined. Always `json_schema`."""



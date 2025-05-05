# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal
from pydantic import BaseModel
__all__ = ["EvalStringCheckGraderParam"]


class EvalStringCheckGraderParam(BaseModel):
    input: str = None
    # old  input: Required[str]
    """The input text. This may include template strings."""

    name: str = None
    # old  name: Required[str]
    """The name of the grader."""

    operation: Literal["eq", "ne", "like", "ilike"] = None
    # old  operation: Required[Literal["eq", "ne", "like", "ilike"]]
    """The string check operation to perform. One of `eq`, `ne`, `like`, or `ilike`."""

    reference: str = None
    # old  reference: Required[str]
    """The reference text. This may include template strings."""

    type: Literal["string_check"] = None
    # old  type: Required[Literal["string_check"]]
    """The object type, which is always `string_check`."""


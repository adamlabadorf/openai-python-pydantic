# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal
from pydantic import BaseModel
__all__ = ["EvalTextSimilarityGraderParam"]


class EvalTextSimilarityGraderParam(BaseModel):
    evaluation_metric:  Literal[ "fuzzy_match", "bleu", "gleu", "meteor", "rouge_1", "rouge_2", "rouge_3", "rouge_4", "rouge_5", "rouge_l" ] = None
    # old  evaluation_metric: Required[ Literal[ "fuzzy_match", "bleu", "gleu", "meteor", "rouge_1", "rouge_2", "rouge_3", "rouge_4", "rouge_5", "rouge_l" ] ]
    """The evaluation metric to use.

    One of `fuzzy_match`, `bleu`, `gleu`, `meteor`, `rouge_1`, `rouge_2`, `rouge_3`,
    `rouge_4`, `rouge_5`, or `rouge_l`.
    """

    input: str = None
    # old  input: Required[str]
    """The text being graded."""

    pass_threshold: float = None
    # old  pass_threshold: Required[float]
    """A float score where a value greater than or equal indicates a passing grade."""

    reference: str = None
    # old  reference: Required[str]
    """The text being graded against."""

    type: Literal["text_similarity"] = None
    # old  type: Required[Literal["text_similarity"]]
    """The type of grader."""

    name: Optional[str] = None
    # old  name: str
    """The name of the grader."""


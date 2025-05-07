# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from pydantic import BaseModel, Field
from typing import List, Optional

from typing import Union,Dict,Optional
from typing_extensions import Literal

__all__ = [
    "CreateEvalJSONLRunDataSourceParam",
    "Source",
    "SourceFileContent",
    "SourceFileContentContent",
    "SourceFileID",
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


Source = Union[SourceFileContent, SourceFileID]


class CreateEvalJSONLRunDataSourceParam(BaseModel):
    source: "Source"
    

    type: "Literal['jsonl']"
    
    """The type of data source. Always `jsonl`."""
SourceFileContentContent.model_rebuild()
SourceFileContent.model_rebuild()
SourceFileID.model_rebuild()
CreateEvalJSONLRunDataSourceParam.model_rebuild()


# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from pydantic import BaseModel, Field
from typing import List, Optional

from typing import Union,Optional,Dict
from typing_extensions import Literal

__all__ = [
    "CreateEvalJSONLRunDataSourceParam",
    "Source",
    "SourceFileContent",
    "SourceFileContentContent",
    "SourceFileID",
]


class SourceFileContentContent(BaseModel):
    item: "Dict[str, object]"= None
    

    sample: "Optional[Dict[str, object]]"= None
    


class SourceFileContent(BaseModel):
    content: "List[SourceFileContentContent]"= None
    
    """The content of the jsonl file."""

    type: "Literal['file_content']"= None
    
    """The type of jsonl source. Always `file_content`."""


class SourceFileID(BaseModel):
    id: "str"= None
    
    """The identifier of the file."""

    type: "Literal['file_id']"= None
    
    """The type of jsonl source. Always `file_id`."""


Source = Union[SourceFileContent, SourceFileID]


class CreateEvalJSONLRunDataSourceParam(BaseModel):
    source: "Source"= None
    

    type: "Literal['jsonl']"= None
    
    """The type of data source. Always `jsonl`."""
SourceFileContentContent.model_rebuild()
SourceFileContent.model_rebuild()
SourceFileID.model_rebuild()
CreateEvalJSONLRunDataSourceParam.model_rebuild()


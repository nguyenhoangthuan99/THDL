from typing import Dict, List, Optional
from pydantic import BaseModel
from enum import Enum
class Source(str,Enum):
    toanmath = "toanmath"

class Response(BaseModel):
    title:str
    link:str
    date:Optional[str] = None
    source:Optional[Source] = None

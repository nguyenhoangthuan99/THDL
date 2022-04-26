from typing import Dict, List, Optional
from pydantic import BaseModel

class RequestSearch(BaseModel):
    subject:Optional[str] = None
    grade:Optional[str] = None
    text:Optional[str]=None
    
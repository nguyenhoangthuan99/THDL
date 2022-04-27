from typing import Dict, List, Optional
from pydantic import BaseModel
from enum import Enum

class Response(BaseModel):
    title:str
    link:str
    date:Optional[str] = None

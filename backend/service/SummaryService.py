from model.responses import Response
import asyncio
from fastapi import HTTPException
from typing import List
class SummaryService:
    def __init__(self,):
        pass
    async def summary(self,list_object:list):
        return list_object
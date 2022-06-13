from model.responses import Response
import asyncio
from fastapi import HTTPException
from typing import List
class SummaryService:
    def __init__(self,):
        pass
    async def summary(self,list_object:list):# [a,b,c,d,e] -> [[a],[b,c],[d,e]]
        ###
        ###
        list_object = [ list_object[i:i+5] for i in range(0, len(list_object), 5)
]
      
        return list_object

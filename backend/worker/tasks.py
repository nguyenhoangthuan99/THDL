from .get_celery import get_celery
import asyncio
from config import Settings
import time,sys
from service.factory import FACTORY
from model.request import RequestSearch
settings = Settings()
sys.path.append("..")
celery = get_celery()
import os
if os.environ.get("MODE") == "worker":
    loop = asyncio.get_event_loop()
@celery.task(bind=True)
def run_session(self, req:dict,engine:str):
    engine = FACTORY[engine]()
    loop = asyncio.get_event_loop()
    results = loop.run_until_complete(engine.process(RequestSearch(**req)))
    #loop.close()
    return results
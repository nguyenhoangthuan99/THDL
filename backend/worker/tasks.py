from .get_celery import get_celery
import asyncio
from config import Settings
import time,sys
from service.factory import FACTORY
from model.request import RequestSearch
settings = Settings()
sys.path.append("..")
celery = get_celery()

@celery.task(bind=True)
def run_session(self, req:dict,engine:str):
    engine = FACTORY[engine]()
    results = engine.process(RequestSearch(**req))
    return results
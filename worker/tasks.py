import requests
from .get_celery import get_celery
import asyncio
from config import Settings
import time,sys
settings = Settings()
sys.path.append("..")
celery = get_celery()

@celery.task(bind=True)
def run_session(self, data:dict):
    time.sleep(30)
    return "done"
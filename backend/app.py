from fastapi.middleware.cors import CORSMiddleware
from fastapi import (
    APIRouter, FastAPI, Request,
    HTTPException,
    Header,
    Depends,
    Response as HttpResponse,
    Query,
)
from fastapi.responses import HTMLResponse
from starlette.responses import RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from model.request import RequestSearch
from config import Settings
from worker.get_celery import get_celery, a_get_result
from worker import tasks
import uuid
import uvicorn, celery
app = FastAPI()

app.add_middleware(
	CORSMiddleware,
	allow_origins=["*"],
	allow_credentials=True,
	allow_methods=["*"],
	allow_headers=["*"],
)
settings = Settings()
@app.post("/search")
async def search(req:RequestSearch):
    final = {}
    for web in settings.list_webpage:
        job_id = str(web)+"-"+ str(uuid.uuid4())
        result = tasks.run_session.apply_async(
                args=[
                    req.dict(),
                    web
                    
                ],
                task_id=job_id,
            )
        final[web] = job_id
    return final
    
@app.post("/search/{web}")
async def search_one_web(req:RequestSearch,web:str):
    final = {}
    
    job_id = str(web)+"-"+ str(uuid.uuid4())
    result = tasks.run_session.apply_async(
            args=[
                req.dict(),
                web
                
            ],
            task_id=job_id,
        )
    final[web] = job_id
    return final
@app.get("/list-web-pages")
async def get_list_web_pages():
    return settings.list_webpage


@app.get(
    "/result/{task_id}"
)
async def get_annotate_result(task_id:str):
    try:
        task=celery.result.AsyncResult(task_id)
        return await a_get_result(task)
    except:
        raise HTTPException(status_code=422, detail=f"No tasks found")
@app.get("/", response_class=HTMLResponse)
async def read_item(request: Request):
	return templates.TemplateResponse("index.html", {"request": request})

if __name__ == "__main__":
    uvicorn.run(app, host=settings.host,port=settings.port)
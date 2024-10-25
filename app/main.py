from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from app.routers import data_manager

VERSION = "0.1.0"
DESCRIPTION = "A FastAPI server to for my knowledge repository"


app = FastAPI(version=VERSION, description=DESCRIPTION)

templates = Jinja2Templates(directory="templates")

app.mount("/static", StaticFiles(directory="static"), name="static")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


routers = [data_manager]

for item in routers:
    app.include_router(item.router)


@app.get("/")
async def index(request: Request):
    return templates.TemplateResponse(request=request, name="index.html", context={})


@app.get("/version")
async def version():
    return {"version": VERSION}

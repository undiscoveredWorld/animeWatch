from os import environ
from os import path
from fastapi import FastAPI
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from starlette.requests import Request
from starlette.responses import HTMLResponse
from starlette.templating import _TemplateResponse

BASEDIR = environ.get("BASEDIR") or path.dirname(__file__)

app = FastAPI()

app.mount("/static", StaticFiles(directory="{0}/static".format(BASEDIR)), name="static")
templates = Jinja2Templates(directory="{0}/templates".format(BASEDIR))


@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return render_page("home.html", request)


@app.get("/search", response_class=HTMLResponse)
async def search(request: Request):
    return render_page("search.html", request)


@app.get("/anime", response_class=HTMLResponse)
async def anime(request: Request):
    return render_page("anime.html", request)


@app.get("/registration", response_class=HTMLResponse)
async def registration(request: Request):
    return render_page("registration.html", request)


@app.get("/login", response_class=HTMLResponse)
async def login(request: Request):
    return render_page("login.html", request)


def render_page(page: str, request: Request, context: dict = dict) -> _TemplateResponse:
    """
    Render the page and return the rendered
    :param page: path to the page from /templates/
    :param request: request from end point
    :param context: context for template
    :return:
    """
    finally_context = {"request": request}
    return templates.TemplateResponse(page, finally_context)

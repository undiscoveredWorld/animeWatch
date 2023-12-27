import os

from fastapi import APIRouter, Request
from fastapi import Depends
from starlette.responses import HTMLResponse

from views.render import render_page

router = APIRouter()


@router.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return render_page("home.html", request)


@router.get("/search", response_class=HTMLResponse)
async def search(request: Request):
    return render_page("search.html", request)


@router.get("/anime", response_class=HTMLResponse)
async def anime(request: Request):
    return render_page("anime.html", request)


@router.get("/registration", response_class=HTMLResponse)
async def registration(request: Request):
    return render_page("registration.html", request)

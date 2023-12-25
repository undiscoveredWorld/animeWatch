import os

from fastapi import APIRouter, Request
from fastapi import Depends
from starlette.responses import HTMLResponse

from views.render import render_page

router = APIRouter()


@router.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return render_page("home.html", request)

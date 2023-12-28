from fastapi import APIRouter, Request
from starlette.responses import HTMLResponse

from views.render import render_page
from views.navigation import get_navigation_context
from controllers.navigation import NavigationFromList

router = APIRouter()


def get_generic_context() -> dict:
    return {
        "navigation_elements": get_navigation_context(NavigationFromList)
    }


@router.get("/", response_class=HTMLResponse)
async def home(request: Request):
    context = get_generic_context()
    return render_page("home.html", request, context)


@router.get("/search", response_class=HTMLResponse)
async def search(request: Request):
    return render_page("search.html", request)


@router.get("/anime", response_class=HTMLResponse)
async def anime(request: Request):
    return render_page("anime.html", request)


@router.get("/registration", response_class=HTMLResponse)
async def registration(request: Request):
    return render_page("registration.html", request)


@router.get("/login", response_class=HTMLResponse)
async def login(request: Request):
    return render_page("login.html", request)

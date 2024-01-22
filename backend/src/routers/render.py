"""
Stores routers, that renders page and response it

List of routers:
    home
    search
    anime
    registration
    login
"""

from fastapi import APIRouter, Request
from fastapi import Depends
from starlette.responses import HTMLResponse

from views.navigation import get_navigation_context
from controllers.navigation import NavigationFromSQL

router = APIRouter()


@router.get("/")
async def test(request: Request):
    return {"message": "Hello World"}


def get_generic_context() -> dict:
    """
    Collect all generic context, summarize it and return it
    :return: Completed generic context
    """
    return {
        "navigation_elements": get_navigation_context(NavigationFromSQL)
    }



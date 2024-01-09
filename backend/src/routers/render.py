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
from starlette.responses import HTMLResponse

from views.navigation import get_navigation_context
from controllers.navigation import NavigationFromList

router = APIRouter()


def get_generic_context() -> dict:
    """
    Collect all generic context, summarize it and return it
    :return: Completed generic context
    """
    return {
        "navigation_elements": get_navigation_context(NavigationFromList)
    }



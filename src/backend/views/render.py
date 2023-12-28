"""
Support render view

List of functions:
    render_page -- render the page and returns the rendered
"""

from fastapi import Request
from fastapi.templating import Jinja2Templates
from starlette.templating import _TemplateResponse

import settings

templates = Jinja2Templates(directory="{0}/views/templates".format(settings.BASEDIR))


def render_page(page: str, request: Request, context: dict = dict) -> _TemplateResponse:
    """
    Render the page and return the rendered
    :param page: path to the page from /templates/
    :param request: request from end point
    :param context: context for template
    :return:
    """
    finally_context = {"request": request}
    finally_context.update(context)
    return templates.TemplateResponse(page, finally_context)

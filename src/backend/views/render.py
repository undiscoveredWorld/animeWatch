from fastapi import Request
from fastapi.templating import Jinja2Templates
from starlette.templating import _TemplateResponse

import settings

templates = Jinja2Templates(directory="{0}/views/templates".format(settings.BASEDIR))


def render_page(page: str, request: Request, context: dict = dict) -> _TemplateResponse:
    finally_context = {"request": request}
    finally_context.update(context)
    return templates.TemplateResponse(page, finally_context)

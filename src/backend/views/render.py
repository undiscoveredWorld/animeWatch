from fastapi import Request
from fastapi.templating import Jinja2Templates
from starlette.templating import _TemplateResponse


templates = Jinja2Templates(directory="/home/arch/Programs/golang/animeWatch/src/backend/views/templates")


def render_page(page: str, request: Request) -> _TemplateResponse:
    return templates.TemplateResponse(page, {"request": request})

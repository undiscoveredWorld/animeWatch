"""
The main entry point
"""

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from routers import render
import settings

app = FastAPI()

app.mount("/static", StaticFiles(directory="{0}/views/static".format(settings.BASEDIR)), name="static")

app.include_router(render.router)

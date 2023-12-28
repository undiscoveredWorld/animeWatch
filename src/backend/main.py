from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from routrers import render
import settings

app = FastAPI()

app.mount("/static", StaticFiles(directory="{0}/views/static".format(settings.BASEDIR)), name="static")

app.include_router(render.router)

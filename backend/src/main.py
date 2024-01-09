"""
The main entry point
"""

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from routers import render
import settings

app = FastAPI()


app.include_router(render.router)

import sys

from fastapi import FastAPI, Depends
from fastapi.staticfiles import StaticFiles

from routrers import render

app = FastAPI()

app.mount("/static", StaticFiles(directory="/home/arch/Programs/golang/animeWatch/src/backend/views/static"), name="static")

app.include_router(render.router)

"""
The main entry point
"""

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from routers import render
from models.database.db import Base
from models.database.db import postgres_engine
from models.database.db import SessionLocal
import settings

Base.metadata.create_all(bind=postgres_engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


app = FastAPI()

app.mount("/static", StaticFiles(directory="{0}/views/static".format(settings.BASEDIR)), name="static")

app.include_router(render.router)

"""
The main entry point
"""

from fastapi import FastAPI

from routers import render
from models.database.db import Base
from models.database.db import postgres_engine
from models.database.db import SessionLocal

import models.database.models.anime
import models.database.models.navigation
Base.metadata.create_all(bind=postgres_engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


app = FastAPI()

app.include_router(render.router)

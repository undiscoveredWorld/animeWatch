from fastapi import FastAPI
from sqlalchemy import MetaData

from routers import navigation
from models.database.db import Base
from models.database.db import main_sql_engine


def _create_all_in_metadata(metadata: MetaData) -> None:
    # Needs for working create_all
    import models.database.models.anime
    import models.database.models.navigation
    metadata.create_all(bind=main_sql_engine)


_create_all_in_metadata(Base.metadata)

app = FastAPI()
app.include_router(navigation.router)

from fastapi import FastAPI
from sqlalchemy import MetaData

from navigation.routers import navigation_router
from common.db import Base
from common.db import main_sql_engine


def _create_all_in_metadata(metadata: MetaData) -> None:
    # Needs for working create_all
    import anime.models
    import navigation.models
    metadata.create_all(bind=main_sql_engine)


_create_all_in_metadata(Base.metadata)

app = FastAPI()
app.include_router(navigation_router)

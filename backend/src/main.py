from fastapi import FastAPI
from sqlalchemy import MetaData

from common.db import Base
from common.db import main_sql_engine
from db_filler.routers import filler_router
from navigation.routers import navigation_router


def _create_all_tables_from_metadata(metadata: MetaData) -> None:
    # Needs for working create_all
    import navigation.models
    metadata.create_all(bind=main_sql_engine)


_create_all_tables_from_metadata(Base.metadata)

app = FastAPI()
app.include_router(navigation_router)
app.include_router(filler_router, prefix="/filler")

from fastapi.routing import APIRouter
from fastapi import Depends
from sqlalchemy.orm import Session

from common.main_sql_db import get_main_sql_db
from .filler import fill_main_sql_db_by_debug_rows
from .clearer import clear_main_sql_db


filler_router = APIRouter(tags=["Filler"])


@filler_router.post("/fill")
def fill(db: Session = Depends(get_main_sql_db)):
    fill_main_sql_db_by_debug_rows(db)
    return {"status": "success"}


@filler_router.post("/clear")
def clear(db: Session = Depends(get_main_sql_db)):
    clear_main_sql_db(db)
    return {"status": "success"}

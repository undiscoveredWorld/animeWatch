from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from navigation.cruds import get_all_navigation as crud_get_all_navigation
from common.main_sql_db import get_main_sql_db
from navigation.schemes import NavigationElement

navigation_router = APIRouter()


@navigation_router.get("/get_all_navigation/", response_model=list[NavigationElement])
def get_all_navigation(db: Session = Depends(get_main_sql_db)):
    navigation = crud_get_all_navigation(db)
    return navigation

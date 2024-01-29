from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from navigation.cruds import get_all_navigation as crud_get_all_navigation
from common.db import get_db
from navigation.schemes import NavigationElement

navigation_router = APIRouter()


@navigation_router.get("/get_all_navigation/", response_model=list[NavigationElement])
def get_all_navigation(db: Session = Depends(get_db)):
    navigation = crud_get_all_navigation(db)
    return navigation

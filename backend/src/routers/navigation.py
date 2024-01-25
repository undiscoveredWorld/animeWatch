"""
Stores routers, that renders page and response it

List of routers:
    home
    search
    anime
    registration
    login
"""

from fastapi import APIRouter
from fastapi import Depends
from sqlalchemy.orm import Session

from models.schemes.navigation import NavigationElement
from models.database.db import get_db
from models.database.crud.navigation import get_all_navigation as crud_get_all_navigation


router = APIRouter()


@router.get("/get_all_navigation/", response_model=list[NavigationElement])
def get_all_navigation(db: Session = Depends(get_db)):
    navigation = crud_get_all_navigation(db)
    return navigation

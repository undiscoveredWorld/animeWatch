from sqlalchemy.orm import Session

from models.database.crud._common import return_response_or_raise_exception
from models.database.models import navigation as navigation_models
from models.schemes.navigation import NavigationElement


def get_navigation_by_id(db: Session, navigation_id: int) -> NavigationElement:
    response = db.query(navigation_models.NavigationElement).filter_by(id=navigation_id).first()
    return return_response_or_raise_exception(response)


def get_all_navigation(db: Session) -> list[NavigationElement]:
    response = db.query(navigation_models.NavigationElement).all()
    return return_response_or_raise_exception(response)


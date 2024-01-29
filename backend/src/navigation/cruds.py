from sqlalchemy.orm import Session

import navigation.models
from common.utils import return_response_or_raise_exception
from navigation.schemes import NavigationElement


def get_navigation_by_id(db: Session, navigation_id: int) -> NavigationElement:
    response = db.query(navigation.models.NavigationElement).filter_by(id=navigation_id).first()
    return return_response_or_raise_exception(response)


def get_all_navigation(db: Session) -> list[NavigationElement]:
    response = db.query(navigation.models.NavigationElement).all()
    return return_response_or_raise_exception(response)

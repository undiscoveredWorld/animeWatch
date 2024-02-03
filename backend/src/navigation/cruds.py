from sqlalchemy.orm import Session

import navigation.models
from navigation.schemas import NavigationElement


def get_all_navigation(db: Session) -> list[NavigationElement]:
    response = db.query(navigation.models.NavigationElement).all()
    return response

from sqlalchemy.orm import Session

import navigation.models
from common.utils import return_response_or_raise_exception
from navigation.schemes import NavigationElement


def get_all_navigation(db: Session) -> list[NavigationElement]:
    response = db.query(navigation.models.NavigationElement).all()
    return return_response_or_raise_exception(response)

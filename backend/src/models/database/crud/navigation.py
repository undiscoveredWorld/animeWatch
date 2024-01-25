from sqlalchemy.orm import Session

from models.database.models import navigation as navigation_models
from models.schemes.navigation import NavigationElement
from models.schemes.navigation import NavigationElementBase
from models.schemes.navigation import NavigationElementCreate


def get_navigation_by_id(db: Session, navigation_id: int):
    return db.query(navigation_models.NavigationElement).filter_by(id=navigation_id).first()


def get_all_navigation(db: Session):
    return db.query(navigation_models.NavigationElement).all()

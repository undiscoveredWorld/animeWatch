from sqlalchemy.orm import Session

from models.database.models import navigation as navigation_models
from models.schemes.navigation import NavigationElement
from models.schemes.navigation import NavigationElementBase
from models.schemes.navigation import NavigationElementCreate


def get_navigation_by_id(db: Session, id: int):
    return db.query(navigation_models.NavigationElement).filter_by(id=id).first()


def get_all_navigation(db: Session):
    return db.query().all()

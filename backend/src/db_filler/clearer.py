from sqlalchemy.orm import Session
from sqlalchemy import delete

from navigation.models import NavigationElement as NavigationElementModel


def clear_main_sql_db(db: Session) -> None:
    clear_navigation_table(db)


def clear_navigation_table(db: Session) -> None:
    db.execute(
        delete(NavigationElementModel)
    )
    db.commit()

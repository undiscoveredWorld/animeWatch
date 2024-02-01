from sqlalchemy.orm import Session
from sqlalchemy import insert

from navigation.models import NavigationElement as NavigationElementModel
from navigation.schemes import NavigationElementCreate as NavigationElementSchemeCreate


def fill_main_sql_db_by_debug_rows(db: Session) -> None:
    fill_navigation_table(db)


def fill_navigation_table(db: Session) -> None:
    db.execute(
        insert(NavigationElementModel),
        [
            dict(create_navigation_element_create("OVA", "", "#")),
            dict(create_navigation_element_create("Ongoings", "", "#")),
            dict(create_navigation_element_create("ONA", "", "#"))
        ]
    )
    db.commit()


def create_navigation_element_create(
        name: str,
        description: str,
        url: str) -> NavigationElementSchemeCreate:
    return NavigationElementSchemeCreate(
        name=name, description=description, url=url
    )

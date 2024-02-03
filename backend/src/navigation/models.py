from sqlalchemy import Column, Integer, String

from common.main_sql_db import Base


class NavigationElement(Base):
    __tablename__ = "navigation_elements"

    id = Column(Integer, primary_key=True, unique=True, autoincrement=True, nullable=False)
    name = Column(String, nullable=False, unique=True)
    description = Column(String, nullable=False)
    url = Column(String, nullable=False, default="#")

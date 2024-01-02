from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String

from models.database.db import Base


class NavigationElements(Base):
    __tablename__ = "navigation_elements"

    id = Column(Integer, primary_key=True, unique=True, autoincrement=True, index=True, nullable=False)
    description = Column(String)
    url = Column(String, nullable=False, default="#")


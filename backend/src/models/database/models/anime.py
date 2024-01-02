from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String

from models.database.db import Base
from models.schemes.anime import AnimeStatus


class Genre(Base):
    __tablename__ = "genres"

    id = Column(Integer, primary_key=True, unique=True, nullable=False, autoincrement=True)
    name = Column(String, unique=True, nullable=False)
    description = Column(String)


class AnimeTag(Base):
    __tablename__ = "anime_tags"

    id = Column(Integer, primary_key=True, unique=True, nullable=False, autoincrement=True)
    name = Column(String, unique=True, nullable=False)
    description = Column(String)


class AnimeCategory(Base):
    __tablename__ = "anime_categories"

    id = Column(Integer, primary_key=True, unique=True, nullable=False, autoincrement=True)
    name = Column(String, unique=True, nullable=False)
    description = Column(String)


class Studio(Base):
    __tablename__ = "studios"

    id = Column(Integer, primary_key=True, unique=True, nullable=False, autoincrement=True)
    name = Column(String, unique=True, nullable=False)
    description = Column(String)


class Season(Base):
    __tablename__ = "seasons"

    id = Column(Integer, primary_key=True, unique=True, nullable=False, autoincrement=True)
    name = Column(String, unique=True, nullable=False)
    description = Column(String)

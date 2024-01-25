from sqlalchemy import Column, ForeignKey
from sqlalchemy import Enum
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy.orm import relationship

from models.database.db import Base
from models.schemes.anime import AnimeStatus
from models.schemes.anime import TimesOfYear


class Genre(Base):
    __tablename__ = "genres"

    id = Column(Integer, primary_key=True, unique=True, nullable=False, autoincrement=True)
    name = Column(String, unique=True, nullable=False)
    description = Column(String)

    all_anime = relationship("GenreToAnime", back_populates="genre")


class AnimeTag(Base):
    __tablename__ = "anime_tags"

    id = Column(Integer, primary_key=True, unique=True, nullable=False, autoincrement=True)
    name = Column(String, unique=True, nullable=False)
    description = Column(String)

    all_anime = relationship("TagToAnime", back_populates="anime_tag")


class AnimeCategory(Base):
    __tablename__ = "anime_categories"

    id = Column(Integer, primary_key=True, unique=True, nullable=False, autoincrement=True)
    name = Column(String, unique=True, nullable=False)
    description = Column(String)

    all_anime = relationship("Anime", back_populates="category")


class Studio(Base):
    __tablename__ = "studios"

    id = Column(Integer, primary_key=True, unique=True, nullable=False, autoincrement=True)
    name = Column(String, unique=True, nullable=False)
    description = Column(String)

    all_anime = relationship("Anime", back_populates="studio")


class Season(Base):
    __tablename__ = "seasons"

    id = Column(Integer, primary_key=True, unique=True, nullable=False, autoincrement=True)
    year = Column(Integer, unique=True, nullable=False)
    time_of_year = Column(Enum(TimesOfYear), nullable=False)

    all_anime = relationship("Anime", back_populates="season")
    all_seasons_of_anime = relationship("SeasonOfAnime", back_populates="season")


class GenreToAnime(Base):
    __tablename__ = "genre_to_anime"

    id = Column(Integer, primary_key=True, unique=True, nullable=False, autoincrement=True)
    anime_id = Column(Integer, ForeignKey("anime.id"))
    genre_id = Column(Integer, ForeignKey("genres.id"))

    anime = relationship("Anime", back_populates="genres")
    genre = relationship("Genre", back_populates="all_anime")


class TagToAnime(Base):
    __tablename__ = "tag_to_anime"

    id = Column(Integer, primary_key=True, unique=True, nullable=False, autoincrement=True)
    anime_id = Column(Integer, ForeignKey("anime.id"))
    anime_tag_id = Column(Integer, ForeignKey("anime_tags.id"))

    anime = relationship("Anime", back_populates="tags")
    anime_tag = relationship("AnimeTag", back_populates="all_anime")


class Anime(Base):
    __tablename__ = "anime"

    id = Column(Integer, primary_key=True, unique=True, nullable=False, autoincrement=True)
    original_name = Column(String, unique=True, nullable=False)
    english_name = Column(String)
    russian_name = Column(String)
    description = Column(String)
    duration_of_series = Column(String)
    age_restriction = Column(String)
    status = Column(Enum(AnimeStatus))
    category_id = Column(Integer, ForeignKey("anime_categories.id"))
    studio_id = Column(Integer, ForeignKey("studios.id"))
    season_id = Column(Integer, ForeignKey("seasons.id"))

    category = relationship("AnimeCategory", back_populates="all_anime")
    studio = relationship("Studio", back_populates="all_anime")
    season = relationship("Season", back_populates="all_anime")
    genres = relationship("GenreToAnime", back_populates="anime")
    tags = relationship("TagToAnime", back_populates="anime")
    seasons = relationship("SeasonOfAnime", back_populates="anime")


class SeasonOfAnime(Base):
    __tablename__ = "seasons_of_anime"

    id = Column(Integer, primary_key=True, unique=True, nullable=False, autoincrement=True)
    n = Column(Integer, nullable=False)
    season_id = Column(Integer, ForeignKey("seasons.id"))
    anime_id = Column(Integer, ForeignKey("anime.id"))

    season = relationship("Season", back_populates="all_seasons_of_anime")
    series = relationship("Series", back_populates="season_of_anime")
    anime = relationship("Anime", back_populates="seasons")


class Series(Base):
    __tablename__ = "series"

    id = Column(Integer, primary_key=True, unique=True, nullable=False, autoincrement=True)
    n = Column(Integer, nullable=False)
    name = Column(String, nullable=True)
    season_of_anime_id = Column(Integer, ForeignKey("seasons_of_anime.id"))

    season_of_anime = relationship("SeasonOfAnime", back_populates="series")
    translates = relationship("Translate", back_populates="series")


class Translate(Base):
    __tablename__ = "translates"

    id = Column(Integer, primary_key=True, unique=True, nullable=False, autoincrement=True)
    name = Column(String, nullable=True)
    series_id = Column(Integer, ForeignKey("series.id"))

    series = relationship("Series", back_populates="translates")
    players = relationship("Player", back_populates="translate")


class Player(Base):
    __tablename__ = "players"

    id = Column(Integer, primary_key=True, unique=True, nullable=False, autoincrement=True)
    name = Column(String, nullable=False)
    url = Column(String, nullable=False, default="#")
    translate_id = Column(Integer, ForeignKey("translates.id"))

    translate = relationship("Translate", back_populates="players")

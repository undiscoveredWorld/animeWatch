from enum import Enum
from typing import Optional
from datetime import datetime
from pydantic import BaseModel

from .auth import User
from .schemes import Model


class TimesOfYear(Enum):
    winter = 1
    spring = 2
    summer = 3
    autumn = 4


class AnimeStatus(Enum):
    released = "released"
    previewed = "previewed"
    ongoing = "ongoing"
    dropped = "dropped"


class GenreBase(BaseModel):
    name: str
    description: str | None


class GenreCreate(GenreBase):
    pass


class Genre(GenreBase):
    id: int
    all_anime: list["Anime"]

    class Config:
        orm_mode = True


class AnimeTagBase(BaseModel):
    name: str
    description: str | None


class AnimeTagCreate(AnimeTagBase):
    pass


class AnimeTag(AnimeTagBase):
    id: int
    all_anime: list["Anime"]

    class Config:
        orm_mode = True


class AnimeCategoryBase(BaseModel):
    name: str
    description: str | None


class AnimeCategoryCreate(AnimeCategoryBase):
    pass


class AnimeCategory(AnimeCategoryBase):
    id: int
    all_anime: list["Anime"]

    class Config:
        orm_mode = True


class StudioBase(BaseModel):
    name: str
    description: Optional[str]


class StudioCreate(StudioBase):
    pass


class Studio(StudioBase):
    id: int
    all_anime: list["Anime"]

    class Config:
        orm_mode = True


class SeasonBase(BaseModel):
    year: int
    time_of_year: TimesOfYear


class SeasonCreate(SeasonBase):
    pass


class Season(SeasonBase):
    id: int
    all_anime: list["Anime"]

    class Config:
        orm_mode = True


class AnimeElement(BaseModel):
    publication_date: datetime
    previewed_date: datetime
    anime_status: AnimeStatus


class AnimeBase(BaseModel):
    previewed_date: datetime | None
    anime_status: AnimeStatus
    original_name: str
    english_name: str | None
    russian_name: str | None
    description: str | None
    duration_of_series: str | None
    age_restriction: str | None


class AnimeCreate(AnimeBase):
    publisher: User
    category: AnimeCategory
    studio: Studio
    season: Season


class Anime(AnimeBase):
    publisher: User
    publication_date: datetime
    category: AnimeCategory
    studio: Studio
    season: Season
    category: AnimeCategory
    studio: Studio
    season: Season
    genres: list[Genre]
    tags: list[AnimeTag]


class SeasonOfAnime(AnimeElement):
    n: int
    anime: Anime
    season: Season


class Series(AnimeElement):
    n: int
    season: SeasonOfAnime
    name: str | None


class Translate(AnimeElement):
    series: Series
    name: str | None


class Player(AnimeElement):
    translate: Translate
    name: str | None
    url: str

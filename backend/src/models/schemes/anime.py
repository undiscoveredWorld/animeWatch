from enum import Enum
from typing import Optional
from datetime import datetime
from pydantic import BaseModel

from .auth import User


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
    id: int
    publisher: User
    publication_date: datetime
    category_id: int
    studio_id: int
    season_id: int
    genres: list[Genre]
    tags: list[AnimeTag]
    seasons: list["SeasonOfAnime"]

    class Config:
        orm_mode = True


class SeasonOfAnimeBase(BaseModel):
    n: int


class SeasonOfAnimeCreate(BaseModel):
    anime: Anime
    season: Season


class SeasonOfAnime(SeasonOfAnimeBase):
    id: int
    n: int
    anime_id: int
    season_id: int
    series: list["Series"]

    class Config:
        orm_mode = True


class SeriesBase(BaseModel):
    n: int
    name: str | None


class SeriesCreate(SeriesBase):
    season: SeasonOfAnime


class Series(SeriesBase):
    id: int
    season_id: int
    translates: list["Translate"]

    class Config:
        orm_mode = True


class TranslateBase(BaseModel):
    name: str | None


class TranslateCreate(TranslateBase):
    series: Series


class Translate(TranslateBase):
    id: int
    series_id: int
    players: list["Player"]

    class Config:
        orm_mode = True


class PlayerBase(BaseModel):
    name: str | None
    url: str


class PlayerCreate(PlayerBase):
    translate: Translate


class Player(PlayerBase):
    id: int
    translate_id: int

    class Config:
        orm_mode = True

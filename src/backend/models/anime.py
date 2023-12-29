from enum import Enum
from pydantic import BaseModel
from datetime import datetime

from auth import User


class AnimeStatus(Enum):
    released = "released"
    previewed = "previewed"
    ongoing = "ongoing"
    dropped = "dropped"


class Genre(BaseModel):
    name: str
    description: str | None


class AnimeTag(BaseModel):
    name: str
    description: str | None


class AnimeCategory(BaseModel):
    name: str
    description: str | None


class Studio(BaseModel):
    name: str
    description: str | None


class Season(BaseModel):
    year: int
    timeOfYear: int


class AnimeElement(BaseModel):
    publicationDate: datetime
    previewedDate: datetime
    status: AnimeStatus


class Anime(AnimeElement):
    publisher: User
    originalName: str
    englishName: str | None
    russianName: str | None
    description: str | None
    durationOfSeries: str | None
    ageRestriction: str | None
    tags: list[AnimeTag] | None
    genres: list[Genre] | None
    studio: Studio | None
    seasonOfPublication: Season


class SeasonOfAnime(AnimeElement):
    n: int
    anime: Anime
    season: Season


class Series(AnimeElement):
    n: int
    season: SeasonOfAnime
    name: str | None

from enum import Enum
from typing import Type
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


class AnimeShort(AnimeElement):
    originalName: str

    def get_seasons(self) -> list["SeasonOfAnime"]:
        raise NotImplemented("Not implemented")

    def get_series(self) -> list["Series"]:
        raise NotImplemented("Not implemented")


class Anime(AnimeShort):
    publisher: User
    englishName: str | None
    russianName: str | None
    description: str | None
    durationOfSeries: str | None
    ageRestriction: str | None
    tags: list[AnimeTag] | None
    genres: list[Genre] | None
    studio: Studio | None
    seasonOfPublication: Season | None


class SeasonOfAnime(AnimeElement):
    n: int
    anime: Type[AnimeShort]
    season: Season


class Series(AnimeElement):
    n: int
    season: SeasonOfAnime
    name: str | None

from enum import Enum
from typing import Optional
from datetime import datetime

from .auth import User
from models.core.schemes import Model


class AnimeStatus(Enum):
    released = "released"
    previewed = "previewed"
    ongoing = "ongoing"
    dropped = "dropped"


class Genre(Model):
    name: str
    description: str | None


class AnimeTag(Model):
    name: str
    description: str | None


class AnimeCategory(Model):
    name: str
    description: str | None


class Studio(Model):
    name: str
    description: Optional[str]


class Season(Model):
    year: int
    timeOfYear: int


class AnimeElement(Model):
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

    class Meta:
        name = "anime"


class SeasonOfAnime(AnimeElement):
    n: int
    anime_id: int
    season_id: int

    class Meta:
        name = "seasonOfAnime"
        FKs = ["anime_id", "season_id"]


class Series(AnimeElement):
    n: int
    season: SeasonOfAnime
    name: str | None

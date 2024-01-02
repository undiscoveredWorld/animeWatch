from enum import Enum
from typing import Optional
from datetime import datetime

from .auth import User
from .schemes import Model


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
    publication_date: datetime
    previewed_date: datetime
    anime_status: AnimeStatus


class Anime(AnimeElement):
    publisher: User
    original_name: str
    english_name: str | None
    russian_name: str | None
    description: str | None
    duration_of_series: str | None
    age_restriction: str | None
    category: AnimeCategory
    studio: Studio
    season: Season

    def get_seasons(self) -> list["SeasonOfAnime"]:
        raise NotImplemented("Not implemented")

    def get_series(self) -> list["Series"]:
        raise NotImplemented("Not implemented")


class SeasonOfAnime(AnimeElement):
    n: int
    anime: Anime
    season: Season


class Series(AnimeElement):
    n: int
    season: SeasonOfAnime
    name: str | None

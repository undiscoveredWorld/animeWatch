from datetime import datetime
from typing import Any, List

from pydantic import BaseModel

from anime.enums import TimesOfYear, AnimeStatus
from common.mongo_base_schema import MongoBase


class AnimeGenreBase(MongoBase):
    __table_name__ = "genres"

    name: str
    description: str


class AnimeGenreCreate(AnimeGenreBase):
    pass


class AnimeGenre(AnimeGenreBase):
    class Config:
        from_attributes = True


class AnimeTagBase(MongoBase):
    __table_name__ = "tags"

    name: str
    description: str


class AnimeTagCreate(AnimeTagBase):
    pass


class AnimeTag(AnimeTagBase):
    class Config:
        from_attributes = True


class AnimeCategoryBase(MongoBase):
    __table_name__ = "categories"

    name: str
    description: str


class AnimeCategoryCreate(AnimeCategoryBase):
    pass


class AnimeCategory(AnimeCategoryBase):
    class Config:
        from_attributes = True


class AnimeStudioBase(MongoBase):
    __table_name__ = "studios"

    name: str
    description: str


class AnimeStudioCreate(AnimeStudioBase):
    pass


class AnimeStudio(AnimeStudioBase):
    class Config:
        from_attributes = True


class SeasonBase(MongoBase):
    __table_name__ = "seasons"

    year: int
    time_of_year: TimesOfYear

    class Config:
        use_enum_values = True


class SeasonCreate(SeasonBase):
    pass


class Season(SeasonBase):
    class Config:
        from_attributes = True


class AnimeBase(MongoBase):
    __table_name__ = "anime"

    original_name: str
    english_name: str
    russian_name: str

    publication_date: datetime
    previewed_date: datetime
    anime_status: AnimeStatus
    description: str
    duration_of_series: str
    age_restriction: str

    publisher_id: int
    category_id: Any
    studio_id: Any
    season_id: Any

    genres_id: List[Any]
    tags_id: List[Any]
    anime_seasons_id: List[Any]

    class Config:
        use_enum_values = True


class AnimeCreate(AnimeBase):
    pass


class Anime(AnimeBase):
    class Config:
        from_attributes = True


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
    series: list["AnimeSeries"]

    class Config:
        from_attributes = True


class AnimeSeriesBase(BaseModel):
    n: int
    name: str


class AnimeSeriesCreate(AnimeSeriesBase):
    season: SeasonOfAnime


class AnimeSeries(AnimeSeriesBase):
    id: int
    season_id: int
    translates: list["AnimeTranslate"]

    class Config:
        from_attributes = True


class AnimeTranslateBase(BaseModel):
    name: str


class AnimeTranslateCreate(AnimeTranslateBase):
    series: AnimeSeries


class AnimeTranslate(AnimeTranslateBase):
    id: int
    series_id: int
    players: list["AnimeVideoPlayer"]

    class Config:
        from_attributes = True


class AnimeVideoPlayerBase(BaseModel):
    name: str
    url: str


class AnimeVideoPlayerCreate(AnimeVideoPlayerBase):
    translate: AnimeTranslate


class AnimeVideoPlayer(AnimeVideoPlayerBase):
    id: int
    translate_id: int

    class Config:
        from_attributes = True
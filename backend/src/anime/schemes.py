from datetime import datetime
from pydantic import BaseModel

from anime.enums import TimesOfYear, AnimeStatus
from auth.schemes import User
from common.mongo_base_schema import MongoBase


class AnimeGenreBase(MongoBase):
    name: str
    description: str


class AnimeGenreCreate(AnimeGenreBase):
    pass


class AnimeGenre(AnimeGenreBase):
    class Config:
        from_attributes = True


class AnimeTagBase(MongoBase):
    name: str
    description: str


class AnimeTagCreate(AnimeTagBase):
    pass


class AnimeTag(AnimeTagBase):
    class Config:
        from_attributes = True


class AnimeCategoryBase(MongoBase):
    name: str
    description: str


class AnimeCategoryCreate(AnimeCategoryBase):
    pass


class AnimeCategory(AnimeCategoryBase):
    class Config:
        from_attributes = True


class AnimeStudioBase(MongoBase):
    name: str
    description: str


class AnimeStudioCreate(AnimeStudioBase):
    pass


class AnimeStudio(AnimeStudioBase):
    class Config:
        from_attributes = True


class SeasonBase(MongoBase):
    year: int
    time_of_year: TimesOfYear


class SeasonCreate(SeasonBase):
    pass


class Season(SeasonBase):
    class Config:
        from_attributes = True


class AnimeBase(BaseModel):
    original_name: str
    english_name: str
    russian_name: str

    publication_date: datetime
    previewed_date: datetime
    anime_status: AnimeStatus
    description: str
    duration_of_series: str
    age_restriction: str

    publisher: User
    category: AnimeCategory
    studio: AnimeStudio
    season: Season


class AnimeCreate(AnimeBase):
    pass


class Anime(AnimeBase):
    id: int
    genres: list[AnimeGenre]
    tags: list[AnimeTag]
    seasons: list["SeasonOfAnime"]

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

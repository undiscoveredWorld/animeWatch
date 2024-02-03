from motor.motor_asyncio import AsyncIOMotorClient

from .schemes import AnimeGenreCreate, AnimeGenre
from .schemes import AnimeTagCreate, AnimeTag
from .schemes import AnimeCategoryCreate, AnimeCategory
from .schemes import AnimeStudioCreate, AnimeStudio
from .schemes import SeasonCreate, Season


async def create_genre(db: AsyncIOMotorClient, genre: AnimeGenreCreate) -> AnimeGenre:
    await db["genres"].insert_one(genre.model_dump_for_mongo())
    new_genre = AnimeGenre(**genre.model_dump())
    return new_genre


async def update_genre(db: AsyncIOMotorClient, genre: AnimeGenreCreate) -> AnimeGenre:
    await db["genres"].update_one(
        {
            "_id": genre.id
        },
        {
            "$set": genre.model_dump(
                exclude={'id'}
            )
        }
    )
    new_genre = AnimeGenre(**genre.model_dump())
    return new_genre


async def create_tag(db: AsyncIOMotorClient, tag: AnimeTagCreate) -> AnimeTag:
    await db["tags"].insert_one(tag.model_dump_for_mongo())
    new_tag = AnimeTag(**tag.model_dump())
    return new_tag


async def create_category(db: AsyncIOMotorClient, category: AnimeCategoryCreate) -> AnimeCategory:
    await db["categories"].insert_one(category.model_dump_for_mongo())
    new_category = AnimeCategory(**category.model_dump())
    return new_category


async def create_studio(db: AsyncIOMotorClient, study: AnimeStudioCreate) -> AnimeStudio:
    await db["studies"].insert_one(study.model_dump_for_mongo())
    new_study = AnimeStudio(**study.model_dump())
    return new_study


async def create_season(db: AsyncIOMotorClient, season: SeasonCreate) -> Season:
    await db["seasons"].insert_one(season.model_dump_for_mongo())
    new_season = Season(**season.model_dump())
    return new_season

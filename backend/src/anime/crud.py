from motor.motor_asyncio import AsyncIOMotorClient

from .schemes import AnimeGenreCreate, AnimeGenre
from .schemes import AnimeTagCreate, AnimeTag


async def create_genre(db: AsyncIOMotorClient, genre: AnimeGenreCreate) -> AnimeGenre:
    await db["genres"].insert_one(genre.model_dump_for_mongo())
    new_genre = AnimeGenre(**genre.model_dump())
    return new_genre


async def create_tag(db: AsyncIOMotorClient, tag: AnimeTagCreate) -> AnimeTag:
    await db["tags"].insert_one(tag.model_dump_for_mongo())
    new_tag = AnimeTag(**tag.model_dump())
    return new_tag

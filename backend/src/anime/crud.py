from motor.motor_asyncio import AsyncIOMotorClient

from .schemes import AnimeGenreCreate, AnimeGenre


async def create_genre(db: AsyncIOMotorClient, genre: AnimeGenreCreate) -> AnimeGenre:
    await db["genres"].insert_one(genre.model_dump())
    new_genre = AnimeGenre(**genre.model_dump())
    return new_genre

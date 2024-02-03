from motor.motor_asyncio import AsyncIOMotorClient
from pymongo.results import InsertOneResult

from .schemes import AnimeGenreCreate, AnimeGenre


async def create_genre(db: AsyncIOMotorClient, genre: AnimeGenreCreate) -> AnimeGenre:
    inserting_result: InsertOneResult = await db["genres"].insert_one(genre.model_dump())
    new_genre = AnimeGenre(
        **genre.model_dump(),
        id=str(inserting_result.inserted_id.binary)
    )
    return new_genre

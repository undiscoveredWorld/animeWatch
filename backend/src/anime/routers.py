from fastapi.routing import APIRouter
from fastapi import Depends
from motor.motor_asyncio import AsyncIOMotorClient

from .crud import create_genre as crud_create_genre
from .schemes import AnimeGenreCreate, AnimeGenre
from common.main_mongo_db import get_main_mongo_db

anime_router = APIRouter()


@anime_router.post("/create_genre", response_model=AnimeGenre)
async def create_genre(genre: AnimeGenreCreate, db: AsyncIOMotorClient = Depends(get_main_mongo_db)) -> AnimeGenre:
    return await crud_create_genre(db, genre)

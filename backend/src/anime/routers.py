from fastapi.routing import APIRouter
from fastapi import Depends
from motor.motor_asyncio import AsyncIOMotorClient
from pymongo.errors import DuplicateKeyError

from .crud import create_genre as crud_create_genre
from .crud import create_tag as crud_create_tag
from .schemes import AnimeGenreCreate, AnimeGenre
from .schemes import AnimeTagCreate, AnimeTag
from common.main_mongo_db import get_main_mongo_db
from common.errors import InsertDuplicateInstanceException
from common.mongo_base_schema import MongoBase

anime_router = APIRouter()


@anime_router.post("/create_genre", response_model=AnimeGenre)
async def create_genre(genre: AnimeGenreCreate, db: AsyncIOMotorClient = Depends(get_main_mongo_db)) -> AnimeGenre:
    try:
        return await crud_create_genre(db, genre)
    except DuplicateKeyError:
        raise_insert_duplicated_instance_exception(genre)


@anime_router.post("/create_tag", response_model=AnimeTag)
async def create_tag(tag: AnimeTagCreate, db: AsyncIOMotorClient = Depends(get_main_mongo_db)) -> AnimeTag:
    try:
        return await crud_create_tag(db, tag)
    except DuplicateKeyError:
        raise_insert_duplicated_instance_exception(tag)


def raise_insert_duplicated_instance_exception(schema: MongoBase):
    raise InsertDuplicateInstanceException(
        details=f"Inserted duplicated {schema.__class__.__name__} instance",
        code=400,
        location={
            "class": schema.__class__.__name__
        }
    )

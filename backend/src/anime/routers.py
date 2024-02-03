from fastapi.routing import APIRouter
from fastapi import Depends
from motor.motor_asyncio import AsyncIOMotorClient
from pymongo.errors import DuplicateKeyError

from .crud import create_genre as crud_create_genre
from .crud import update_genre as crud_update_genre
from .crud import create_tag as crud_create_tag
from .crud import create_category as crud_create_category
from .crud import create_studio as crud_create_studio
from .crud import create_season as crud_create_season
from .schemes import AnimeGenreCreate, AnimeGenre
from .schemes import AnimeTagCreate, AnimeTag
from .schemes import AnimeCategoryCreate, AnimeCategory
from .schemes import AnimeStudioCreate, AnimeStudio
from .schemes import SeasonCreate, Season
from common.main_mongo_db import get_main_mongo_db
from common.errors import InsertDuplicateInstanceException
from common.mongo_base_schema import MongoBase

anime_router = APIRouter()


@anime_router.post("/create_genre", response_model=AnimeGenre)
async def create_genre(
        genre: AnimeGenreCreate,
        db: AsyncIOMotorClient = Depends(get_main_mongo_db)
) -> AnimeGenre:
    try:
        return await crud_create_genre(db, genre)
    except DuplicateKeyError:
        raise_insert_duplicated_instance_exception(genre)


@anime_router.put("/update_genre", response_model=AnimeGenre)
async def update_genre(
        genre: AnimeGenreCreate,
        db: AsyncIOMotorClient = Depends(get_main_mongo_db)
) -> AnimeGenre:
    return await crud_update_genre(db, genre)


@anime_router.post("/create_tag", response_model=AnimeTag)
async def create_tag(tag: AnimeTagCreate, db: AsyncIOMotorClient = Depends(get_main_mongo_db)) -> AnimeTag:
    try:
        return await crud_create_tag(db, tag)
    except DuplicateKeyError:
        raise_insert_duplicated_instance_exception(tag)


@anime_router.post("/create_category", response_model=AnimeCategory)
async def create_category(
        category: AnimeCategoryCreate,
        db: AsyncIOMotorClient = Depends(get_main_mongo_db)
) -> AnimeCategory:
    try:
        return await crud_create_category(db, category)
    except DuplicateKeyError:
        raise_insert_duplicated_instance_exception(category)


@anime_router.post("/create_studio", response_model=AnimeStudio)
async def create_studio(
        studio: AnimeStudioCreate,
        db: AsyncIOMotorClient = Depends(get_main_mongo_db)
) -> AnimeStudio:
    try:
        return await crud_create_studio(db, studio)
    except DuplicateKeyError:
        raise_insert_duplicated_instance_exception(studio)


@anime_router.post("/create_season", response_model=Season)
async def create_season(
        season: SeasonCreate,
        db: AsyncIOMotorClient = Depends(get_main_mongo_db)
) -> Season:
    try:
        return await crud_create_season(db, season)
    except DuplicateKeyError:
        raise_insert_duplicated_instance_exception(season)


def raise_insert_duplicated_instance_exception(schema: MongoBase):
    raise InsertDuplicateInstanceException(
        details=f"Inserted duplicated {schema.__class__.__name__} instance",
        code=400,
        location={
            "class": schema.__class__.__name__
        }
    )

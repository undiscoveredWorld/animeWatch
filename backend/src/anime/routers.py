from fastapi.routing import APIRouter
from fastapi import Depends
from motor.motor_asyncio import AsyncIOMotorClient
from pymongo.errors import DuplicateKeyError
from starlette.responses import JSONResponse

from .crud import create_mongo_model
from .crud import update_mongo_model
from .crud import delete_mongo_model
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
        result = await create_mongo_model(db, genre)
        new_genre = AnimeGenre(**result)
        return new_genre
    except DuplicateKeyError:
        raise_insert_duplicated_instance_exception(genre)


@anime_router.put("/update_genre", response_model=AnimeGenre)
async def update_genre(
        genre: AnimeGenreCreate,
        db: AsyncIOMotorClient = Depends(get_main_mongo_db)
) -> AnimeGenre:
    result = await update_mongo_model(db, genre)
    new_genre = AnimeGenre(**result)
    return new_genre


@anime_router.delete("/delete_genre")
async def delete_genre(genre: AnimeGenre, db: AsyncIOMotorClient=Depends(get_main_mongo_db)) -> JSONResponse:
    await delete_mongo_model(db, genre)
    return JSONResponse(
        status_code=200,
        content={}
    )


@anime_router.post("/create_tag", response_model=AnimeTag)
async def create_tag(tag: AnimeTagCreate, db: AsyncIOMotorClient = Depends(get_main_mongo_db)) -> AnimeTag:
    try:
        result = await create_mongo_model(db, tag)
        new_tag = AnimeTag(**result)
        return new_tag
    except DuplicateKeyError:
        raise_insert_duplicated_instance_exception(tag)


@anime_router.post("/create_category", response_model=AnimeCategory)
async def create_category(
        category: AnimeCategoryCreate,
        db: AsyncIOMotorClient = Depends(get_main_mongo_db)
) -> AnimeCategory:
    try:
        result = await create_mongo_model(db, category)
        new_category = AnimeCategory(**result)
        return new_category
    except DuplicateKeyError:
        raise_insert_duplicated_instance_exception(category)


@anime_router.post("/create_studio", response_model=AnimeStudio)
async def create_studio(
        studio: AnimeStudioCreate,
        db: AsyncIOMotorClient = Depends(get_main_mongo_db)
) -> AnimeStudio:
    try:
        result = await create_mongo_model(db, studio)
        new_studio = AnimeStudio(**result)
        return new_studio
    except DuplicateKeyError:
        raise_insert_duplicated_instance_exception(studio)


@anime_router.post("/create_season", response_model=Season)
async def create_season(
        season: SeasonCreate,
        db: AsyncIOMotorClient = Depends(get_main_mongo_db)
) -> Season:
    try:
        result = await create_mongo_model(db, season)
        new_season = Season(**result)
        return new_season
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

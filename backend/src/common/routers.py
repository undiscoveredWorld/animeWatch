from fastapi import APIRouter
from motor.motor_asyncio import AsyncIOMotorClient
from collections import namedtuple
from typing import Type
from fastapi import Depends
from starlette.responses import JSONResponse
from pymongo.errors import DuplicateKeyError

from anime.crud import (
    create_mongo_model,
    update_mongo_model,
    delete_mongo_model
)
from .main_mongo_db import get_main_mongo_db
from .mongo_base_schema import MongoBase
from .errors import InsertDuplicateInstanceException


ModelTypesForGeneratingRouters = namedtuple(
    typename="ModelTypesForGeneratingRouters",
    field_names=[
        "model_type_for_create",
        "model_type_for_update",
        "model_type_for_delete"
    ]
)


class RouterGenerator:
    router: APIRouter

    def __init__(self, router: APIRouter):
        self.router = router

    def generate_all_end_points(self, path: str, model_types: ModelTypesForGeneratingRouters):
        self.generate_create_end_point(path, model_types.model_type_for_create)
        self.generate_update_end_point(path, model_types.model_type_for_update)
        self.generate_delete_end_point(path, model_types.model_type_for_delete)

    def generate_create_end_point(self, path: str, model_type: Type[MongoBase]) -> None:
        @self.router.post(
            path,
            tags=["Create"],
            responses={
                "400": {"description": f"Cannot create a new {model_type.__name__}"},
                "200": {"description": f"Success create {model_type.__name__}"}
            }
        )
        async def create(
                model: model_type,
                db: AsyncIOMotorClient = Depends(get_main_mongo_db)
        ) -> JSONResponse:
            return await _try_create_mongo_model(db, model)

    def generate_update_end_point(self, path: str, model_type: Type[MongoBase]):
        @self.router.put(
            path,
            tags=["Update"],
            responses={
                "200": {"description": f"Success update {model_type.__name__}"}
            }
        )
        async def update(
                model: model_type,
                db: AsyncIOMotorClient = Depends(get_main_mongo_db)
        ) -> JSONResponse:
            await update_mongo_model(db, model)
            return JSONResponse(
                status_code=200,
                content={}
            )

    def generate_delete_end_point(self, path: str, model_type: Type[MongoBase]):
        @self.router.delete(
            path,
            tags=["Delete"],
            responses={
                "200": {"description": f"Success delete {model_type.__name__}"}
            }
        )
        async def delete(
                model: model_type,
                db: AsyncIOMotorClient = Depends(get_main_mongo_db)
        ) -> JSONResponse:
            await delete_mongo_model(db, model)
            return JSONResponse(
                status_code=200,
                content={}
            )


async def _try_create_mongo_model(db: AsyncIOMotorClient, model: MongoBase) -> JSONResponse:
    try:
        await create_mongo_model(db, model)
        return JSONResponse(
            status_code=201,
            content={}
        )
    except DuplicateKeyError:
        raise_insert_duplicated_instance_exception(model)


def create_model_types(
        model_type_for_create: Type[MongoBase],
        model_type_for_update: Type[MongoBase],
        model_type_for_delete: Type[MongoBase]
):
    model_types = ModelTypesForGeneratingRouters(
        model_type_for_create,
        model_type_for_update,
        model_type_for_delete
    )
    return model_types


def raise_insert_duplicated_instance_exception(schema: MongoBase):
    raise InsertDuplicateInstanceException(
        details=f"Inserted duplicated {schema.__class__.__name__} instance",
        code=400,
        location={
            "class": schema.__class__.__name__
        }
    )

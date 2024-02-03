from motor.motor_asyncio import AsyncIOMotorClient
from typing import Any

from common.mongo_base_schema import MongoBase


async def create_mongo_model(db: AsyncIOMotorClient, model: MongoBase) -> dict[str, Any]:
    await db[model.get_table_name()].insert_one(model.model_dump_for_mongo())
    return model.model_dump()


async def update_mongo_model(db: AsyncIOMotorClient, model: MongoBase) -> dict[str, Any]:
    await db[model.get_table_name()].update_one(
        {
            "_id": model.id
        },
        {
            "$set": model.model_dump(
                exclude={'id'}
            )
        }
    )
    return model.model_dump()


async def delete_mongo_model(db: AsyncIOMotorClient, model: MongoBase):
    await db[model.get_table_name()].delete_one(
        {
            "_id": model.id
        }
    )

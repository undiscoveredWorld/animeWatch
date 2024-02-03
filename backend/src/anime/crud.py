from motor.motor_asyncio import AsyncIOMotorClient
from typing import Any, Callable
from pymongo.errors import (
    ServerSelectionTimeoutError,
    NetworkTimeout,
    ExecutionTimeout,
    WTimeoutError,
    WaitQueueTimeoutError
)

from common.mongo_base_schema import MongoBase
from common.errors import TimeOutException


async def create_mongo_model(db: AsyncIOMotorClient, model: MongoBase) -> dict[str, Any]:
    async def insert_one():
        await db[model.get_table_name()].insert_one(model.model_dump_for_mongo())

    await _except_mongo_timeout(insert_one)

    return model.model_dump()


async def update_mongo_model(db: AsyncIOMotorClient, model: MongoBase) -> dict[str, Any]:
    async def update_one():
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

    await _except_mongo_timeout(update_one)

    return model.model_dump()


async def delete_mongo_model(db: AsyncIOMotorClient, model: MongoBase):
    async def delete_one():
        await db[model.get_table_name()].delete_one(
            {
                "_id": model.id
            }
        )

    await _except_mongo_timeout(delete_one)


async def _except_mongo_timeout(func: Callable) -> Any:
    try:
        return await func()
    except ServerSelectionTimeoutError:
        _raise_time_out_exception()
    except NetworkTimeout:
        _raise_time_out_exception()
    except ExecutionTimeout:
        _raise_time_out_exception()
    except WaitQueueTimeoutError:
        _raise_time_out_exception()
    except WTimeoutError:
        _raise_time_out_exception()


def _raise_time_out_exception():
    raise TimeOutException(
        code=503,
        details="Mongo timed out"
    )

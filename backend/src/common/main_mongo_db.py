from motor.motor_asyncio import AsyncIOMotorClient

from settings import MAIN_MONGO_DB_URL
from settings import MAIN_MONGO_DB_NAME


def get_main_mongo_db():
    client = AsyncIOMotorClient(MAIN_MONGO_DB_URL)
    try:
        yield client[MAIN_MONGO_DB_NAME]
    finally:
        client.close()

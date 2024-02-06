import unittest
import os
import time
from typing import Type, List, Dict

from sqlalchemy import create_engine, bindparam
from sqlalchemy import (
    insert,
    update,
    delete
)
from sqlalchemy import (
    Column,
    Integer,
    String
)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Engine
from sqlalchemy.orm import Session
from pydantic import BaseModel

USER = "postgres"
PASS = "TEST"
DB_NAME = "test"
URL = f"postgresql+psycopg://{USER}:{PASS}@127.0.0.1:5431/{DB_NAME}"

Base = declarative_base()


class ItemModel(Base):
    __tablename__ = "items"

    id = Column(Integer, autoincrement=True, unique=True, primary_key=True, nullable=False)
    name = Column(String, nullable=False)


class ItemBase(BaseModel):
    name: str


class ItemCreate(ItemBase):
    pass


class Item(ItemBase):
    id: int

    class Config:
        from_attributes = True


class PostgresTests(unittest.TestCase):
    engine: Engine
    session: Session

    def test_insert_item(self):
        item_create = ItemCreate(name="Create")
        self._insert_model_into_db(
            model=ItemModel,
            elements=[
                dict(item_create)
            ]
        )
        self._test_inserting(item_create)

    def test_update_item(self):
        item_create = ItemCreate(name="Update")
        self._insert_model_into_db(
            model=ItemModel,
            elements=[
                dict(item_create)
            ]
        )
        self._test_inserting(item_create)

        item = self.session.query(ItemModel).one()
        item_table = ItemModel.metadata.tables["items"]

        stmt = (
            item_table.update()
            .where(item_table.c.id == bindparam("item_id"))
            .values(name="Updated")
        )
        self.session.execute(
            stmt,
            [
                {"item_id": item.id}
            ]
        )
        self.session.commit()

        items = self.session.query(ItemModel).all()
        self.assertEquals(
            len(items),
            1
        )
        self.assertEquals(
            items[0].name,
            "Updated"
        )

    def _insert_model_into_db(self, model: Type[Base], elements: List[Dict]):
        self.session.execute(
            statement=insert(model),
            params=elements
        )
        self.session.commit()

    def _test_inserting(self, item_create):
        result = self.session.query(ItemModel).all()
        self.assertEquals(
            len(result),
            1
        )
        self.assertEquals(
            result[0].name,
            item_create.name
        )

    def tearDown(self):
        super().tearDown()
        self.session.execute(
            delete(ItemModel)
        )
        self.session.commit()

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls._start_postgres()
        cls._init_db()
        Base.metadata.create_all(cls.engine)

    @classmethod
    def tearDownClass(cls):
        super().tearDownClass()
        cls._stop_postgres()

    @classmethod
    def _start_postgres(cls):
        os.system(
            f"docker run -d -p 5431:5432 --rm \
                --env POSTGRES_USER={USER} \
                --env POSTGRES_PASSWORD={PASS} \
                --env POSTGRES_DB={DB_NAME} \
                --name=anime_watch_postgres_test \
                postgres:alpine"
        )
        time.sleep(6)

    @classmethod
    def _stop_postgres(cls):
        os.system("docker stop anime_watch_postgres_test")

    @classmethod
    def _init_db(cls):
        cls.engine = create_engine(URL)
        cls.session = sessionmaker(bind=cls.engine, autoflush=False, autocommit=False)()

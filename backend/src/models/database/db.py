from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from settings import MAIN_SQL_DB_URL

main_sql_engine = create_engine(MAIN_SQL_DB_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=main_sql_engine)

Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

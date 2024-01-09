from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from settings import POSTGRES_URL

postgres_engine = create_engine(
    POSTGRES_URL
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=postgres_engine)

Base = declarative_base()

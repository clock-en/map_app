import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DB_USER = os.environ['MYSQL_USER']
DB_PASSWORD = os.environ['MYSQL_PASSWORD']
DB_HOST = os.environ['MYSQL_HOST']
DB_NAME = os.environ['MYSQL_DB']

SQLALCHEMY_DATABASE_URL = ('mysql+mysqlconnector://{}:{}@{}/{}?charset=utf8mb4'
                           .format(
                               DB_USER,
                               DB_PASSWORD,
                               DB_HOST,
                               DB_NAME
                           ))

engine = create_engine(SQLALCHEMY_DATABASE_URL, pool_recycle=600)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

from sqlalchemy import Column, String
from sqlalchemy.dialects.mysql import INTEGER as Integer
from app.database import Base


class User(Base):
    __tablename__ = 'users'

    id = Column('id', Integer(unsigned=True), primary_key=True, index=True)
    name = Column(String)
    email = Column(String, unique=True, index=True)
    password = Column(String)

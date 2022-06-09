from sqlalchemy import Column, String
from sqlalchemy.dialects.mysql import INTEGER as Integer
from app.core.sqlalchemy.database import Base


class UserDataModel(Base):
    __tablename__ = 'users'

    id = Column('id', Integer(unsigned=True), primary_key=True, index=True)
    name = Column(String)
    email = Column(String, unique=True, index=True)
    password = Column(String)

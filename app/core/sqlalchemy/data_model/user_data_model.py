from datetime import datetime
from sqlalchemy import Column, String, DATETIME
from sqlalchemy.dialects.mysql import INTEGER as Integer
from app.core.sqlalchemy.database import Base


class UserDataModel(Base):
    __tablename__ = 'users'
    __table_args__ = {'extend_existing': True}

    id = Column('id', Integer(unsigned=True), primary_key=True, index=True)
    name = Column(String)
    email = Column(String, unique=True, index=True)
    password = Column(String)
    created_at = Column('created_at', DATETIME, default=datetime.now)
    updated_at = Column('updated_at', DATETIME, default=datetime.now)

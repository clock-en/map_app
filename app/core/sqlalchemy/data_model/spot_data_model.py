from sqlalchemy import Column, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.mysql import INTEGER as Integer
from app.core.sqlalchemy.database import Base


class SpotDataModel(Base):
    __tablename__ = 'spots'
    __table_args__ = {'extend_existing': True}

    id = Column('id', Integer(unsigned=True), primary_key=True, index=True)
    name = Column('name', String, unique=True, index=True)
    description = Column('description', String)
    latitude = Column('latitude', Float)
    longitude = Column('longitude', Float)
    user_id = Column('user_id', Integer(unsigned=True),
                     ForeignKey('users.id', ondelete='CASCADE'))

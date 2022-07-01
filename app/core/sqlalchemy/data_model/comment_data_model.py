from sqlalchemy import Column, String, ForeignKey, DATETIME
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.mysql import INTEGER as Integer
from app.core.sqlalchemy.database import Base
from datetime import datetime


class CommentDataModel(Base):
    __tablename__ = 'comments'
    __table_args__ = {'extend_existing': True}

    id = Column('id', Integer(unsigned=True), primary_key=True, index=True)
    user_id = Column('user_id', Integer(unsigned=True),
                     ForeignKey('users.id', ondelete='CASCADE'))
    spot_id = Column('spot_id', Integer(unsigned=True),
                     ForeignKey('spots.id', ondelete='CASCADE'))
    comment = Column('comment', String)
    created_at = Column('created_at', DATETIME, default=datetime.now)
    updated_at = Column('updated_at', DATETIME, default=datetime.now)
    user = relationship('UserDataModel')

from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.mysql import INTEGER as Integer
from app.core.sqlalchemy.database import Base


class CommentDataModel(Base):
    __tablename__ = 'comments'
    __table_args__ = {'extend_existing': True}

    id = Column('id', Integer(unsigned=True), primary_key=True, index=True)
    user_id = Column('user_id', Integer(unsigned=True),
                     ForeignKey('users.id', ondelete='CASCADE'))
    spot_id = Column('spot_id', Integer(unsigned=True),
                     ForeignKey('spots.id', ondelete='CASCADE'))
    comment = Column('comment', String)


class CommentWithUserDataModel(Base):
    __tablename__ = 'comments'
    __table_args__ = {'extend_existing': True}

    id = Column('id', Integer(unsigned=True), primary_key=True, index=True)
    user_id = Column('user_id', Integer(unsigned=True),
                     ForeignKey('users.id', ondelete='CASCADE'))
    spot_id = Column('spot_id', Integer(unsigned=True),
                     ForeignKey('spots.id', ondelete='CASCADE'))
    comment = Column('comment', String)
    user = relationship('UserDataModel')

from typing import Union
from datetime import datetime
from pydantic import BaseModel, Field, validator
from app.domain.value_object.id import Id
from app.domain.value_object.comment.comment_content import CommentContent
from .users_schema import User
from . import validators


class CommentsBase(BaseModel):
    spot_id: Union[int, str] = Field(example=1)
    comment: str = Field(max_length=CommentContent.MAX_LENGTH,
                         example='コメント文が入る')

    @validator('spot_id')
    def valid_spot_id(cls, v):
        label = 'スポットID'
        validators.valid_id_value(label=label, value=v,
                                  min=Id.MIN_VALUE)
        return v

    @validator('comment')
    def valid_description(cls, v):
        label = 'コメント'
        validators.not_blank(label, v)
        validators.valid_length(label=label, value=v,
                                max=CommentContent.MAX_LENGTH)
        return v


class CommentCreate(CommentsBase):
    pass


class Comment(CommentsBase):
    id: int = Field(example=1)
    user_id: int = Field(example=1)
    created_at: datetime = Field(example='YYYY-MM-DDTHH:MI:SS')
    updated_at: datetime = Field(example='YYYY-MM-DDTHH:MI:SS')
    user: User = Field(
        example={'id': 1, 'name': 'hoge', 'email': 'hoge@example.com'})

    class Config:
        orm_mode = True

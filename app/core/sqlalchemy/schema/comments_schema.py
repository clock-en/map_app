from typing import Union
from pydantic import BaseModel, Field, validator
from app.domain.value_object.comment.comment_content import CommentContent
from . import validators


class CommentsBase(BaseModel):
    spot_id: Union[int, str] = Field(example=1)
    comment: str = Field(max_length=CommentContent.MAX_LENGTH,
                         example='コメント文が入る')

    @validator('comment')
    def valid_description(cls, v):
        label = 'おすすめポイント'
        validators.not_blank(label, v)
        validators.valid_length(label=label, value=v,
                                max=CommentContent.MAX_LENGTH)
        return v

    @validator('spot_id')
    def valid_spot_id(cls, v):
        label = 'スポットID'
        validators.valid_id_value(label, v)


class CommentCreate(CommentsBase):
    pass


class Comment(CommentsBase):
    id: int = Field(example=1)
    user_id: int = Field(example=1)

    class Config:
        orm_mode = True

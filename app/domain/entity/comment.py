from dataclasses import dataclass
from app.domain.value_object.id import Id
from app.domain.value_object.ja_datetime import JaDatetime
from app.domain.value_object.comment.comment_content import CommentContent
from .user import User


@dataclass(init=False, eq=True, frozen=True)
class Comment():
    id: Id
    user_id: Id
    spot_id: Id
    comment: CommentContent
    created_at: JaDatetime
    updated_at: JaDatetime
    user: User

    def __init__(
        self,
        id: Id,
        user_id: Id,
        spot_id: Id,
        comment: CommentContent,
        created_at: JaDatetime,
        updated_at: JaDatetime,
        user: User
    ) -> None:
        object.__setattr__(self, 'id', id)
        object.__setattr__(self, 'user_id', user_id)
        object.__setattr__(self, 'spot_id', spot_id)
        object.__setattr__(self, 'comment', comment)
        object.__setattr__(self, 'created_at', created_at)
        object.__setattr__(self, 'updated_at', updated_at)
        object.__setattr__(self, 'user', user)

from dataclasses import dataclass
from app.domain.value_object.id import Id
from app.domain.value_object.comment.comment_content import CommentContent


@dataclass(init=False, eq=True, frozen=True)
class Comment():
    id: Id
    user_id: Id
    spot_id: Id
    comment: CommentContent

    def __init__(
        self,
        id: Id,
        user_id: Id,
        spot_id: Id,
        comment: CommentContent,
    ) -> None:
        object.__setattr__(self, 'id', id)
        object.__setattr__(self, 'user_id', user_id)
        object.__setattr__(self, 'spot_id', spot_id)
        object.__setattr__(self, 'comment', comment)

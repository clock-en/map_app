from dataclasses import dataclass
from app.domain.value_object.id import Id
from app.domain.value_object.comment.comment_content import CommentContent


@dataclass(init=False, eq=True, frozen=True)
class CreateCommentUsecaseInput(object):
    user_id: Id
    spot_id: Id
    comment: CommentContent

    def __init__(
        self,
        user_id: int,
        spot_id: int,
        comment: str,
    ) -> None:
        object.__setattr__(self, 'user_id', Id(user_id))
        object.__setattr__(self, 'spot_id', Id(spot_id))
        object.__setattr__(self, 'comment', CommentContent(comment))

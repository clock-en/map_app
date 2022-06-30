from typing import Union
from dataclasses import dataclass
from app.domain.entity.comment import Comment
from app.domain.value_object.error.unprocessable_entity_error import (
    UnprocessableEntityError)


@dataclass(init=False, eq=True, frozen=True)
class CreateCommentUsecaseOutput(object):
    is_success: bool
    comment: Union[Comment, None]
    error: Union[UnprocessableEntityError, None]

    def __init__(
        self,
        is_success: bool,
        comment: Comment = None,
        error: UnprocessableEntityError = None
    ) -> None:
        object.__setattr__(self, 'is_success', is_success)
        object.__setattr__(self, 'comment', comment)
        object.__setattr__(self, 'error', error)

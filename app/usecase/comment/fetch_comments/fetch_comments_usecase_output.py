from typing import Union, List
from dataclasses import dataclass
from app.domain.entity.comment import Comment
from app.domain.value_object.error.unprocessable_entity_error import (
    UnprocessableEntityError)


@dataclass(init=False, eq=True, frozen=True)
class FetchCommentsUsecaseOutput(object):
    is_success: bool
    comments: Union[List[Comment], None]
    error: Union[UnprocessableEntityError, None]

    def __init__(
        self,
        is_success: bool,
        comments: Comment = None,
        error: UnprocessableEntityError = None
    ) -> None:
        object.__setattr__(self, 'is_success', is_success)
        object.__setattr__(self, 'comments', comments)
        object.__setattr__(self, 'error', error)

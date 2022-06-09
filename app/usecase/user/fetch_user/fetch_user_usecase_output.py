from typing import Union, List
from dataclasses import dataclass
from app.domain.entity.user import User
from app.domain.value_object.error.notfound_error import (
    NotFoundError)


@dataclass(init=False, eq=True, frozen=True)
class FetchUserUsecaseOutput(object):
    is_success: bool
    user: Union[List[User], None]
    error: Union[NotFoundError, None]

    def __init__(
        self,
        is_success: bool,
        user: User = None,
        error: NotFoundError = None
    ) -> None:
        object.__setattr__(self, 'is_success', is_success)
        object.__setattr__(self, 'user', user)
        object.__setattr__(self, 'error', error)

from typing import Union
from dataclasses import dataclass
from app.domain.entity.user import User
from app.domain.value_object.error.unprocessable_entity_error import (
    UnprocessableEntityError)


@dataclass(init=False, eq=True, frozen=True)
class CreateUserUsecaseOutput(object):
    is_success: bool
    user: Union[User, None]
    error: Union[UnprocessableEntityError, None]

    def __init__(
        self,
        is_success: bool,
        user: User = None,
        error: UnprocessableEntityError = None
    ) -> None:
        object.__setattr__(self, 'is_success', is_success)
        object.__setattr__(self, 'user', user)
        object.__setattr__(self, 'error', error)

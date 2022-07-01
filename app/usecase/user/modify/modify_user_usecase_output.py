from typing import Union
from dataclasses import dataclass
from app.domain.entity.user import User
from app.domain.value_object.error.conflict_error import ConflictError


@dataclass(init=False, eq=True, frozen=True)
class ModifyUserUsecaseOutput(object):
    is_success: bool
    user: Union[User, None]
    error: Union[ConflictError, None]

    def __init__(
        self,
        is_success: bool,
        user: User = None,
        error: ConflictError = None
    ) -> None:
        object.__setattr__(self, 'is_success', is_success)
        object.__setattr__(self, 'user', user)
        object.__setattr__(self, 'error', error)

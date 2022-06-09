from typing import Union
from dataclasses import dataclass
from app.domain.value_object.error.unauthorized_error import (
    UnauthorizedError)


@dataclass(init=False, eq=True, frozen=True)
class LoginUsecaseOutput(object):
    is_success: bool
    access_token: Union[str, None]
    identified_token: Union[str, None]
    expires: Union[str, None]
    error: Union[UnauthorizedError, None]

    def __init__(
        self,
        is_success: bool,
        access_token: str = None,
        identified_token: str = None,
        expires: str = None,
        error: UnauthorizedError = None
    ) -> None:
        object.__setattr__(self, 'is_success', is_success)
        object.__setattr__(self, 'access_token', access_token)
        object.__setattr__(self, 'identified_token', identified_token)
        object.__setattr__(self, 'expires', expires)
        object.__setattr__(self, 'error', error)

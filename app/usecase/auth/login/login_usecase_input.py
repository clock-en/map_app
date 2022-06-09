from dataclasses import dataclass
from app.domain.value_object.email import Email
from app.domain.value_object.password import Password


@dataclass(init=False, eq=True, frozen=True)
class LoginUsecaseInput(object):
    email: Email
    password: Password

    def __init__(
        self,
        email: str,
        password: str,
    ) -> None:
        object.__setattr__(self, 'email', Email(email))
        object.__setattr__(self, 'password', Password(password))

from dataclasses import dataclass
from app.domain.value_object.email import Email
from app.domain.value_object.password import Password
from app.domain.value_object.user.user_name import UserName


@dataclass(init=False, eq=True, frozen=True)
class NewUser():

    name: UserName
    email: Email
    password: Password

    def __init__(
        self,
        name: str,
        email: str,
        password: str,
    ) -> None:
        object.__setattr__(self, 'name', UserName(name))
        object.__setattr__(self, 'email', Email(email))
        object.__setattr__(self, 'password', Password(password))

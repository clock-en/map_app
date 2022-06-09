from dataclasses import dataclass
from app.domain.value_object.id import Id
from app.domain.value_object.email import Email
from app.domain.value_object.hased_password import HashedPassword
from app.domain.value_object.user.user_name import UserName


@dataclass(init=False, eq=True, frozen=True)
class User():
    id: Id
    name: UserName
    email: Email
    password: HashedPassword

    def __init__(
        self,
        id: Id,
        name: UserName,
        email: Email,
        password: HashedPassword
    ) -> None:
        object.__setattr__(self, 'id', id)
        object.__setattr__(self, 'name', name)
        object.__setattr__(self, 'email', email)
        object.__setattr__(self, 'password', password)

from dataclasses import dataclass
from datetime import datetime
from app.domain.value_object.id import Id
from app.domain.value_object.email import Email
from app.domain.value_object.ja_datetime import JaDatetime
from app.domain.value_object.user.user_name import UserName


@dataclass(init=False, eq=True, frozen=True)
class ModifyUserUsecaseInput(object):
    id: Id
    name: UserName
    email: Email
    updated_at: JaDatetime

    def __init__(
        self,
        id: int,
        name: str,
        email: str,
        updated_at: datetime,
    ) -> None:
        object.__setattr__(self, 'id', Id(id))
        object.__setattr__(self, 'name', UserName(name))
        object.__setattr__(self, 'email', Email(email))
        object.__setattr__(self, 'updated_at', JaDatetime(updated_at))

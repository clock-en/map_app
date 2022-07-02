from dataclasses import dataclass
from typing import Union
from app.domain.value_object.id import Id


@dataclass(init=False, eq=True, frozen=True)
class FetchSpotUsecaseInput(object):
    id: Id
    user_id: Id
    editable: Union[bool, None]

    def __init__(
        self,
        id: int,
        user_id: int,
        editable: Union[bool, None]
    ) -> None:
        object.__setattr__(self, 'id', Id(id))
        object.__setattr__(self, 'user_id', Id(user_id))
        object.__setattr__(self, 'editable', editable)

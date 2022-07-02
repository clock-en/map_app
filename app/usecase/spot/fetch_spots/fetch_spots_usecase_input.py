from typing import Union
from dataclasses import dataclass
from app.domain.value_object.id import Id


@dataclass(init=False, eq=True, frozen=True)
class FetchSpotsUsecaseInput(object):
    user_id: Id
    is_own: Union[bool, None] = None

    def __init__(
        self,
        user_id: Union[int, None],
        is_own: Union[bool, None]
    ) -> None:
        object.__setattr__(self, 'user_id', Id(user_id))
        object.__setattr__(self, 'is_own', is_own)

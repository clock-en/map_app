from typing import Union
from dataclasses import dataclass
from app.domain.value_object.id import Id


@dataclass(init=False, eq=True, frozen=True)
class FetchSpotsUsecaseInput(object):
    user_id: Union[Id, None] = None

    def __init__(
        self,
        user_id: Union[int, None]
    ) -> None:
        if (user_id is not None):
            object.__setattr__(self, 'user_id', Id(user_id))

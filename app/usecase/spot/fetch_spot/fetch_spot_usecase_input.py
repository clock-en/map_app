from dataclasses import dataclass
from app.domain.value_object.id import Id


@dataclass(init=False, eq=True, frozen=True)
class FetchSpotUsecaseInput(object):
    user_id: Id

    def __init__(
        self,
        user_id: int
    ) -> None:
        object.__setattr__(self, 'user_id', Id(user_id))

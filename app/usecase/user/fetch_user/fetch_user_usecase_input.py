from dataclasses import dataclass
from app.domain.value_object.id import Id


@dataclass(init=False, eq=True, frozen=True)
class FetchUserUsecaseInput(object):
    id: Id

    def __init__(
        self,
        id: int
    ) -> None:
        object.__setattr__(self, 'id', Id(id))

from dataclasses import dataclass
from app.domain.value_object.id import Id


@dataclass(init=False, eq=True, frozen=True)
class FetchCommentsUsecaseInput(object):
    spot_id: Id = None

    def __init__(
        self,
        spot_id: Id
    ) -> None:
        object.__setattr__(self, 'spot_id', Id(spot_id))

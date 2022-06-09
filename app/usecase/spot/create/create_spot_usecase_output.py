from typing import Union
from dataclasses import dataclass
from app.domain.entity.spot import Spot
from app.domain.value_object.error.unprocessable_entity_error import (
    UnprocessableEntityError)


@dataclass(init=False, eq=True, frozen=True)
class CreateSpotUsecaseOutput(object):
    is_success: bool
    spot: Union[Spot, None]
    error: Union[UnprocessableEntityError, None]

    def __init__(
        self,
        is_success: bool,
        spot: Spot = None,
        error: UnprocessableEntityError = None
    ) -> None:
        object.__setattr__(self, 'is_success', is_success)
        object.__setattr__(self, 'spot', spot)
        object.__setattr__(self, 'error', error)

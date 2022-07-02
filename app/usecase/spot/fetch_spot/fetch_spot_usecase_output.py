from typing import Union, List
from dataclasses import dataclass
from app.domain.entity.spot import Spot
from app.domain.value_object.error.bad_request_error import BadRequestError
from app.domain.value_object.error.notfound_error import (
    NotFoundError)


@dataclass(init=False, eq=True, frozen=True)
class FetchSpotUsecaseOutput(object):
    is_success: bool
    spot: Union[List[Spot], None]
    error: Union[NotFoundError, BadRequestError, None]

    def __init__(
        self,
        is_success: bool,
        spot: Spot = None,
        error: Union[NotFoundError, BadRequestError] = None
    ) -> None:
        object.__setattr__(self, 'is_success', is_success)
        object.__setattr__(self, 'spot', spot)
        object.__setattr__(self, 'error', error)

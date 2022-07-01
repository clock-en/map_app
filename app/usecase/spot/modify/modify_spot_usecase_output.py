from typing import Union
from dataclasses import dataclass
from app.domain.entity.spot import Spot
from app.domain.value_object.error.unprocessable_entity_error import (
    UnprocessableEntityError)
from app.domain.value_object.error.bad_request_error import BadRequestError
from app.domain.value_object.error.conflict_error import ConflictError


@dataclass(init=False, eq=True, frozen=True)
class ModifySpotUsecaseOutput(object):
    is_success: bool
    spot: Union[Spot, None]
    error: Union[UnprocessableEntityError,
                 BadRequestError, ConflictError, None]

    def __init__(
        self,
        is_success: bool,
        spot: Spot = None,
        error: Union[UnprocessableEntityError,
                     BadRequestError, ConflictError] = None
    ) -> None:
        object.__setattr__(self, 'is_success', is_success)
        object.__setattr__(self, 'spot', spot)
        object.__setattr__(self, 'error', error)

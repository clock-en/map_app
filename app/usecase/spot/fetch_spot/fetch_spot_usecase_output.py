from typing import Union, List
from dataclasses import dataclass
from app.domain.entity.spot import SpotWithComments
from app.domain.value_object.error.notfound_error import (
    NotFoundError)


@dataclass(init=False, eq=True, frozen=True)
class FetchSpotUsecaseOutput(object):
    is_success: bool
    spot: Union[List[SpotWithComments], None]
    error: Union[NotFoundError, None]

    def __init__(
        self,
        is_success: bool,
        spot: SpotWithComments = None,
        error: NotFoundError = None
    ) -> None:
        object.__setattr__(self, 'is_success', is_success)
        object.__setattr__(self, 'spot', spot)
        object.__setattr__(self, 'error', error)

from dataclasses import dataclass
from typing import ClassVar


@dataclass(init=False, eq=True, frozen=True)
class Latitude(object):
    value: float

    MIN_VALUE: ClassVar[float] = -90
    MAX_VALUE: ClassVar[float] = 90
    RANGE_ERROR_MESSAGE: ClassVar[str] = 'Invalid latitude value.'

    def __init__(self, value: float) -> None:
        if self.__is_invalid_value(value):
            raise ValueError(self.__class__.__name__ + ':',
                             self.RANGE_ERROR_MESSAGE)
        object.__setattr__(self, 'value', value)

    def __is_invalid_value(self, value: float):
        return value < self.MIN_VALUE or self.MAX_VALUE < value

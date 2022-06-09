from dataclasses import dataclass
from typing import ClassVar


@dataclass(init=False, eq=True, frozen=True)
class Id(object):
    value: int

    MIN_VALUE: ClassVar[int] = 1
    MIN_ERROR_MESSAGE: ClassVar[str] = 'It must be greater than 1.'

    def __init__(self, value: int) -> None:
        if self.__is_invalid_value(value):
            raise ValueError(self.__class__.__name__ + ':',
                             self.MIN_ERROR_MESSAGE)
        object.__setattr__(self, 'value', value)

    def __is_invalid_value(self, value: float):
        return value < self.MIN_VALUE

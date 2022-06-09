from dataclasses import dataclass
from typing import ClassVar


@dataclass(init=False, eq=True, frozen=True)
class SpotName():
    value: str

    MAX_LENGTH: ClassVar[int] = 50
    LENGTH_ERROR_MESSAGE: ClassVar[str] = 'It must be 50 characters or less.'

    def __init__(self, value: str) -> None:
        if self.__is_invalid_length(value):
            raise ValueError(self.__class__.__name__ + ':',
                             self.LENGTH_ERROR_MESSAGE)
        object.__setattr__(self, 'value', value)

    def __is_invalid_length(self, value: str) -> bool:
        return len(value) > self.MAX_LENGTH

from dataclasses import dataclass
from typing import ClassVar
import re


@dataclass(init=False, eq=True, frozen=True)
class Email(object):
    value: str

    EMAIL_REGEXP: ClassVar[str] = (
        r'^[0-9a-zA-Z_.+-]+@[0-9a-zA-Z-]+\.[0-9a-zA-Z-.]+$')
    MAX_LENGTH: ClassVar[int] = 255
    FORMAT_ERROR_MESSAGE: ClassVar[str] = 'Invalid e-mail format.'
    LENGTH_ERROR_MESSAGE: ClassVar[str] = 'It must be 50 characters or less.'

    def __init__(self, value: str) -> None:
        if self.__is_invalid_format(value):
            raise ValueError(self.__class__.__name__ + ':',
                             self.FORMAT_ERROR_MESSAGE)
        if self.__is_invalid_length(value):
            raise ValueError(self.__class__.__name__ + ':',
                             self.LENGTH_ERROR_MESSAGE)
        object.__setattr__(self, 'value', value)

    def __is_invalid_format(self, value: str) -> bool:
        return re.match(self.EMAIL_REGEXP, value) is None

    def __is_invalid_length(self, value: str) -> bool:
        return len(value) > self.MAX_LENGTH

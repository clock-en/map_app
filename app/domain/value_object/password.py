from dataclasses import dataclass
from typing import ClassVar
import re


@dataclass(init=False, eq=True, frozen=True)
class Password():
    value: str

    PASSWORD_REG_EXP: ClassVar[str] = (
        r'\A(?=.*?[a-z])(?=.*?\d)(?=.*?[!-/:-@[-`{-~])[!-~]{8,100}\Z(?i)')
    MAX_LENGTH: ClassVar[int] = 100
    FORMAT_ERROR_MESSAGE: ClassVar[str] = 'Invalid password format.'
    LENGTH_ERROR_MESSAGE: ClassVar[str] = 'It must be 100 characters or less.'

    def __init__(self, value: str) -> None:
        if self.__is_invalid_format(value):
            raise ValueError(self.__class__.__name__ + ':',
                             self.FORMAT_ERROR_MESSAGE)
        if self.__is_invalid_length(value):
            raise ValueError(self.__class__.__name__ + ':',
                             self.LENGTH_ERROR_MESSAGE)
        object.__setattr__(self, 'value', value)

    def __is_invalid_format(self, value: str) -> bool:
        return re.match(self.PASSWORD_REG_EXP, value) is None

    def __is_invalid_length(self, value: str) -> bool:
        return len(value) > self.MAX_LENGTH

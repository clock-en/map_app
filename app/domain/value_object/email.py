from dataclasses import dataclass
from typing import ClassVar
import re


@dataclass(init=False, eq=True, frozen=True)
class Email(object):
    EMAIL_REGEXP: ClassVar[str] = (
        r'^[0-9a-zA-Z_.+-]+@[0-9a-zA-Z-]+\.[0-9a-zA-Z-.]+$')
    MAX_LENGTH: ClassVar[int] = 255
    FORMAT_ERROR_MESSAGE: ClassVar[str] = 'メールアドレスの形式が正しくありません。'
    LENGTH_ERROR_MESSAGE: ClassVar[str] = 'メールアドレスは255字以内で入力してください'

    def __init__(self, value: str) -> None:
        if self.__is_invalid_format(value):
            raise ValueError(self.FORMAT_ERROR_MESSAGE)
        if self.__is_invalid_length(value):
            raise ValueError(self.LENGTH_ERROR_MESSAGE)
        object.__setattr__(self, 'value', value)

    def __is_invalid_format(self, value: str) -> bool:
        return re.match(self.EMAIL_REGEXP, value) is None

    def __is_invalid_length(self, value: str) -> bool:
        return len(value) > self.MAX_LENGTH

from dataclasses import dataclass
from typing import ClassVar
import re


@dataclass(init=False, eq=True, frozen=True)
class Password():
    PASSWORD_REG_EXP: ClassVar[str] = (
        r'/\A(?=.*?[a-z])(?=.*?\d)[a-z\d]{8,100}+\z/i')
    MAX_LENGTH: ClassVar[int] = 20
    FORMAT_ERROR_MESSAGE: ClassVar[str] = 'パスワードの形式が正しくありません。'
    LENGTH_ERROR_MESSAGE: ClassVar[str] = 'パスワードは20字以内で入力してください'

    def __init__(self, value: str) -> None:
        if self.__is_invalid_format(value):
            raise ValueError(self.FORMAT_ERROR_MESSAGE)
        if self.__is_invalid_length(value):
            raise ValueError(self.LENGTH_ERROR_MESSAGE)
        object.__setattr__(self, 'value', value)

    def __is_invalid_format(self, value: str) -> bool:
        return re.match(self.PASSWORD_REG_EXP, value) is None

    def __is_invalid_length(self, value: str) -> bool:
        return len(value) > self.MAX_LENGTH

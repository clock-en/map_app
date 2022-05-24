from dataclasses import dataclass
from typing import ClassVar


@dataclass(init=False, eq=True, frozen=True)
class UserName():
    MAX_LENGTH: ClassVar[int] = 50
    LENGTH_ERROR_MESSAGE: ClassVar[str] = 'ユーザー名は50文字以内で入力してください'

    def __init__(self, value: str) -> None:
        if self.__is_invalid_length(value):
            raise ValueError(self.LENGTH_ERROR_MESSAGE)
        self.value = value

    def __is_invalid_length(self, value: str) -> bool:
        return len(value) > self.MAX_LENGTH

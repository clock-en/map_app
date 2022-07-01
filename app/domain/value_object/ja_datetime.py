from datetime import datetime
from dataclasses import dataclass
from typing import ClassVar


@dataclass(init=False, eq=True, frozen=True)
class JaDatetime():
    value: datetime

    DEFAULT_FORMAT: ClassVar[str] = '%Y-%m-%d %H:%M:%S'
    FORMAT_ERROR_MESSAGE: ClassVar[str] = 'It is invalid format.'

    def __init__(self, value: datetime) -> None:
        object.__setattr__(self, 'value', value)

from dataclasses import dataclass
from typing import Union, ClassVar


@dataclass(init=False, eq=True, frozen=True)
class ConflictError(object):
    message: Union[str, None]
    type: Union[str, None]

    TYPE_CODE: ClassVar[str] = 'CONFLICT'

    def __init__(self, message: str = None) -> None:
        object.__setattr__(self, 'message', message)
        object.__setattr__(self, 'type', self.TYPE_CODE)

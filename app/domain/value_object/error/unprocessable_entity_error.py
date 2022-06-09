from dataclasses import dataclass
from typing import Union, ClassVar


@dataclass(init=False, eq=True, frozen=True)
class UnprocessableEntityError(object):
    field: Union[str, None]
    message: Union[str, None]
    type: Union[str, None]

    TYPE_CODE: ClassVar[str] = 'UNPROCESSABLE_ENTITY'

    def __init__(self, field: str = None, message: str = None) -> None:
        object.__setattr__(self, 'field', field)
        object.__setattr__(self, 'message', message)
        object.__setattr__(self, 'type', self.TYPE_CODE)

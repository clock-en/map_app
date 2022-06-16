from dataclasses import dataclass
from passlib.context import CryptContext
from .password import Password


@dataclass(init=False, eq=True, frozen=True)
class HashedPassword():
    value: str
    pwd_context: CryptContext

    def __init__(self, value: str) -> None:
        object.__setattr__(self, 'value', value)
        object.__setattr__(self, 'pwd_context', CryptContext(
            schemes=['bcrypt'], deprecated='auto'))

    def verify(self, password: Password):
        return self.pwd_context.verify(password, self.value)

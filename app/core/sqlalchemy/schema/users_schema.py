from pydantic import BaseModel, Field, EmailStr
from app.domain.value_object.user.user_name import UserName
from app.domain.value_object.password import Password


class UserBase(BaseModel):
    name: str = Field(max_length=UserName.MAX_LENGTH, example='hoge')
    email: EmailStr = Field(example='hoge@example.com')


class UserCreate(UserBase):
    password: str = Field(
        regex=Password.PASSWORD_REG_EXP,
        min_length=Password.MIN_LENGTH,
        max_length=Password.MAX_LENGTH,
        example='test-1234')


class User(UserBase):
    id: int = Field(example=1)

    class Config:
        orm_mode = True

import re
from pydantic import BaseModel, Field, validator
from app.domain.value_object.user.user_name import UserName
from app.domain.value_object.password import Password
from app.domain.value_object.email import Email
from . import validators


class UserBase(BaseModel):
    name: str = Field(example='hoge')
    email: str = Field(example='hoge@example.com')

    @validator('name')
    def valid_name(cls, v):
        label = 'ユーザー名'
        validators.not_blank(label, v)
        validators.valid_length(label=label, value=v, max=UserName.MAX_LENGTH)
        return v

    @validator('email')
    def valid_email(cls, v):
        label = 'メールアドレス'
        validators.not_blank(label, v)
        validators.valid_length(label=label, value=v, max=UserName.MAX_LENGTH)
        if re.match(Email.EMAIL_REGEXP, v) is None:
            raise ValueError('メールアドレス形式で入力してください')
        return v


class UserCreate(UserBase):
    password: str = Field(example='test-1234')

    @validator('password')
    def valid_password(cls, v):
        label = 'パスワード'
        validators.not_blank(label, v)
        validators.valid_length(
            label=label,
            value=v,
            min=Password.MIN_LENGTH,
            max=Password.MAX_LENGTH
        )
        if re.match(Password.PASSWORD_REG_EXP, v) is None:
            raise ValueError('パスワードは英数字と記号で入力してください')
        return v


class User(UserBase):
    id: int = Field(example=1)

    class Config:
        orm_mode = True

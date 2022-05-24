from pydantic import BaseModel, Field, EmailStr


class UserBase(BaseModel):
    name: str = Field(max_length=50, example='hoge')
    email: EmailStr = Field(example='hoge@example.com')


class UserCreate(UserBase):
    password: str = Field(
        regex=(
            r'\A(?=.*?[a-z])(?=.*?\d)(?=.*?[!-/:-@[-`{-~])[!-~]{8,100}\Z(?i)'),
        min_length=8,
        max_length=20,
        example='test1234')


class User(UserBase):
    id: int = Field(example=1)

    class Config:
        orm_mode = True

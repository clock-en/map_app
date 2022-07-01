from app.domain.value_object.ja_datetime import JaDatetime
from app.infrastructure.dao.user_dao import UserDao
from app.domain.entity.user import User
from app.domain.value_object.id import Id
from app.domain.value_object.email import Email
from app.domain.value_object.hased_password import HashedPassword
from app.domain.value_object.user.user_name import UserName
from app.domain.value_object.user.new_user import NewUser


class UserRepository(object):
    __user_dao: UserDao

    def __init__(self) -> None:
        self.__user_dao = UserDao()

    def create(self, new_user: NewUser) -> User:
        db_user = self.__user_dao.create_user(new_user)
        return User(
            id=Id(db_user.id),
            name=UserName(db_user.name),
            email=Email(db_user.email),
            password=HashedPassword(db_user.password),
            created_at=JaDatetime(db_user.created_at),
            updated_at=JaDatetime(db_user.updated_at)
        )

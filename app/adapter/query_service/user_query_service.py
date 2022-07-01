from typing import Union
from app.core.sqlalchemy.data_model.user_data_model import UserDataModel
from app.domain.entity.user import User
from app.domain.value_object.id import Id
from app.domain.value_object.email import Email
from app.domain.value_object.hased_password import HashedPassword
from app.domain.value_object.ja_datetime import JaDatetime
from app.domain.value_object.user.user_name import UserName
from app.infrastructure.dao.user_dao import UserDao


class UserQueryService(object):
    __user_dao: UserDao

    def __init__(self) -> None:
        self.__user_dao = UserDao()

    def fetch_user_by_email(self, email: Email) -> Union[User, None]:
        return self.__create_user_entity(
            self.__user_dao.get_user_by_email(email))

    def fetch_user_by_id(self, id: Id) -> Union[User, None]:
        return self.__create_user_entity(self.__user_dao.get_user_by_id(id))

    def __create_user_entity(
        self,
        db_user: Union[UserDataModel, None]
    ) -> Union[User, None]:
        if db_user is None:
            return None
        return User(
            id=Id(db_user.id),
            name=UserName(db_user.name),
            email=Email(db_user.email),
            password=HashedPassword(db_user.password),
            created_at=JaDatetime(db_user.created_at),
            updated_at=JaDatetime(db_user.updated_at)
        )

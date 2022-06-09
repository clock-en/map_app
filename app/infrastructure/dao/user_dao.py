from passlib.context import CryptContext
from app.core.sqlalchemy.data_model.user_data_model import UserDataModel
from app.domain.value_object.id import Id
from app.domain.value_object.email import Email
from app.domain.value_object.user.new_user import NewUser
from .dao import Dao


class UserDao(Dao):
    __pwd_context: CryptContext

    def __init__(self) -> None:
        super().__init__()
        self.__pwd_context = CryptContext(
            schemes=['bcrypt'], deprecated='auto')

    def get_user_by_email(self, email: Email):
        return self.db.query(UserDataModel).filter(
            UserDataModel.email == email.value).first()

    def get_user_by_id(self, id: Id):
        return self.db.query(UserDataModel).filter(
            UserDataModel.id == id.value).first()

    def create_user(self, user: NewUser):
        hashed_password = self.__pwd_context.hash(user.password.value)
        new_user = UserDataModel(
            name=user.name.value,
            email=user.email.value,
            password=hashed_password
        )
        self.db.add(new_user)
        self.db.commit()
        self.db.refresh(new_user)
        return new_user

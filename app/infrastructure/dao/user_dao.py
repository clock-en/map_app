from app.model import users_model
from app.schema import users_schema
from passlib.context import CryptContext
from .dao import Dao


class UserDao(Dao):
    __pwd_context: CryptContext

    def get_user_by_email(self, email: str):
        return self.db.query(users_model.User).filter(
            users_model.User.email == email).first()

    def get_user_by_id(self, id: int):
        return self.db.query(users_model.User).filter(
            users_model.User.id == id).first()

    def create_user(self, user: users_schema.UserCreate):
        hashed_password = self.__pwd_context.hash(user.password)
        new_user = users_model.User(
            name=user.name,
            email=user.email,
            password=hashed_password
        )
        self.db.add(new_user)
        self.db.commit()
        self.db.refresh(new_user)
        return new_user

from sqlalchemy.orm import Session

from app.model import users_model
from app.schema import users_schema
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=['bcrypt'], deprecated='auto')


def get_user_by_email(db: Session, email: str):
    return db.query(users_model.User).filter(
        users_model.User.email == email).first()


def get_user_by_id(db: Session, id: int):
    return db.query(users_model.User).filter(
        users_model.User.id == id).first()


def create_user(db: Session, user: users_schema.UserCreate):
    hashed_password = pwd_context.hash(user.password)
    new_user = users_model.User(
        name=user.name,
        email=user.email,
        password=hashed_password
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

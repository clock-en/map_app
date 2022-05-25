from sqlalchemy.orm import Session

from app.model import users_model
from app.schema import users_schemas
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=['bcrypt'], deprecated='auto')


def get_user(db: Session, user_id: int):
    return db.query(users_model.User).filter(
        users_model.User.id == user_id).first()


def get_user_by_email(db: Session, email: str):
    return db.query(users_model.User).filter(
        users_model.User.email == email).first()


def create_user(db: Session, user: users_schemas.UserCreate):
    hashed_password = pwd_context.hash(user.password)
    db_user = users_model.User(name=user.name, email=user.email,
                               password=hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

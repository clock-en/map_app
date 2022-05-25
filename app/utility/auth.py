from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from passlib.context import CryptContext
from sqlalchemy.orm import Session
from app.crud import users_crud
from app.database import get_db

oauth2_scheme = OAuth2PasswordBearer(tokenUrl='api/auth/login')
pwd_context = CryptContext(schemes=['bcrypt'], deprecated='auto')


def verify_password(plain_password: str, hashed_password: str):
    return pwd_context.verify(plain_password, hashed_password)


def get_password_hash(password: str):
    return pwd_context.hash(password)


def authenticate_user(
        db: Session, email: str, password: str,):
    db_user = users_crud.get_user_by_email(db, email)
    if not db_user:
        return False
    if not verify_password(password, db_user.hashed_password):
        return False
    return True


# TODO: 後で修正
def fake_decode_token(db, token):
    # This doesn't provide any security at all
    # Check the next version
    user = users_crud.get_user_by_email(db, token)
    return user


async def get_current_user(
        token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    user = fake_decode_token(db, token)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail='Invalid authentication credentials',
            headers={'WWW-Authenticate': 'Bearer'},
        )
    return user

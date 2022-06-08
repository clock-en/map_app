import os
import hashlib
from typing import Union
from fastapi import Depends, Response, Header, HTTPException, status
from passlib.context import CryptContext
from jose import JWTError, jwt
from datetime import datetime, timedelta
from sqlalchemy.orm import Session
from app.crud import users_crud
from app.database import get_db
from app.schema import auth_schema
from starlette.requests import Request

SECRET_KEY = os.environ['SECRET_KEY']
ALGORITHM = 'HS256'
ACCESS_TOKEN_EXPIRE_MINUTES = 30


oauth2_scheme = auth_schema.OAuth2PasswordBearerWithCookie(
    tokenUrl='api/auth/login')
pwd_context = CryptContext(schemes=['bcrypt'], deprecated='auto')


def verify_password(plain_password: str, hashed_password: str):
    return pwd_context.verify(plain_password, hashed_password)


def get_password_hash(password: str):
    return pwd_context.hash(password)


def authenticate_user(
    db: Session,
    email: str,
    password: str
):
    db_user = users_crud.get_user_by_email(db, email)
    if not db_user:
        return None
    if not verify_password(password, db_user.password):
        return None
    return db_user


def create_credentials_exception():
    return HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail='Could not validate credentials',
        headers={'WWW-Authenticate': 'Bearer'},
    )


async def authorize_user(
    response: Response,
    token: str = Depends(oauth2_scheme),
    db: Session = Depends(get_db)
):
    credentials_exception = create_credentials_exception()
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        user_id: int = int(payload.get('sub'))
        if user_id is None:
            raise credentials_exception
        token_data = auth_schema.TokenData(id=user_id)
    except JWTError:
        raise credentials_exception
    user = users_crud.get_user_by_id(db, id=token_data.id)
    if user is None:
        raise credentials_exception
    expires = create_access_token_expires()
    access_token = create_access_token(user.id, expires)
    set_access_token_cookie(response, access_token, expires)

    return user


def authorize_with_x_token(
    user: str = Depends(authorize_user),
    x_token: Union[str, None] = Header(Defalt=None)
):
    credentials_exception = create_credentials_exception()
    if x_token is None:
        raise credentials_exception
    identified_token = create_identified_token(user.id)
    if x_token != identified_token:
        raise credentials_exception
    return user


def create_access_token(id: int, expires: str):
    data = {'sub': str(id), 'exp': expires}
    encoded_jwt = jwt.encode(data, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


def create_access_token_expires():
    return datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)


def create_identified_token(user_id: int):
    # リクエスト時のカスタムヘッダー用にユーザーごとに固定となるトークンを発行する
    identified_string = os.environ['TOKEN_SALT'] + str(user_id)
    return hashlib.sha512(identified_string.encode("utf-8")).hexdigest()


def validate_content_type(request: Request):
    content_type = request.headers.get("content-type", None)
    if content_type != "application/json":
        raise HTTPException(
            status.HTTP_415_UNSUPPORTED_MEDIA_TYPE,
            f"Unsupported media type: {content_type}."
            " It must be application/json",
        )


def set_access_token_cookie(
    response: Response,
    access_token: str,
    expires: str
):
    response.set_cookie(
        key='access_token',
        value=f'Bearer {access_token}',
        httponly=True,
        secure=False if os.environ['APP_ENV'] == 'DEV' else True,
        samesite='lax',
        expires=expires.strftime("%a, %d %b %Y %H:%M:%S GMT"),
    )

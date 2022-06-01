import os
from fastapi import APIRouter, Depends, Response, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from datetime import datetime
from app.database import get_db
from app.utility import auth

router = APIRouter(prefix='/api/auth', tags=['auth'])


@router.post('/login')
async def login(
    response: Response,
    form_data: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(get_db)
):
    db_user = auth.authenticate_user(
        db, form_data.username, form_data.password)
    if db_user is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail='Incorrect username or password',
            headers={'WWW-Authenticate': 'Bearer'}
        )
    access_token_expires = auth.create_access_token_expires()
    access_token = auth.create_access_token(
        data={'sub': str(db_user.id)}
    )
    expires = datetime.utcnow() + access_token_expires

    response.set_cookie(
        key='access_token',
        value=f'Bearer {access_token}',
        httponly=True,
        secure=False if os.environ['APP_ENV'] == 'DEV' else True,
        samesite='lax',
        expires=expires.strftime("%a, %d %b %Y %H:%M:%S GMT"),
    )
    # リクエスト時のカスタムヘッダー用にユーザーごとに固定となるトークンを発行する
    identified_token = auth.create_identified_token(db_user.id)
    return {'token': identified_token}

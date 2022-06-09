from fastapi import APIRouter, Depends, Response, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from app.core.sqlalchemy.database import get_db
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

    expires = auth.create_access_token_expires()
    access_token = auth.create_access_token(db_user.id, expires)
    auth.set_access_token_cookie(response, access_token, expires)

    # リクエスト時のカスタムヘッダー用にユーザーごとに固定となるトークンを発行する
    identified_token = auth.create_identified_token(db_user.id)
    return {'token': identified_token}


@router.post('/logout')
async def logout(response: Response):
    response.delete_cookie('access_token')
    return {'isLoggedOut': True}

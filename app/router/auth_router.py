from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from app.database import get_db
from app.utility import auth

router = APIRouter(prefix='/api/auth', tags=['auth'])


@router.post('/login')
async def login(
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
        data={'sub': db_user.email}, expires_delta=access_token_expires
    )
    return {'access_token': access_token, 'token_type': 'bearer'}

from fastapi import (
    APIRouter,
    Depends,
    HTTPException)
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from app.database import get_db
from app.crud import users_crud
from app.utility import auth

router = APIRouter(prefix='/api/auth', tags=['auth'])


@router.post('/login')
async def login(
        form_data: OAuth2PasswordRequestForm = Depends(),
        db: Session = Depends(get_db)):
    db_user = users_crud.get_user_by_email(db, form_data.username)
    if not db_user:
        raise HTTPException(
            status_code=400, detail='Incorrect username or password')
    if not auth.verify_password(form_data.password, db_user.password):
        raise HTTPException(
            status_code=400, detail='Incorrect username or password')

    return {'access_token': db_user.email, 'token_type': 'bearer'}

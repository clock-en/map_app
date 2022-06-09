from fastapi import APIRouter, Depends, Response, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from app.usecase.auth import LoginUsecaseInput, LoginUsecaseInteractor
from app.adapter.presenter.auth import LoginPresenter
from app.core.sqlalchemy.database import get_db
from app.domain.value_object.error.unauthorized_error import UnauthorizedError
from app.utility import auth

router = APIRouter(prefix='/api/auth', tags=['auth'])


@router.post('/login')
async def login(
    response: Response,
    form_data: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(get_db)
):
    input = LoginUsecaseInput(
        email=form_data.username,
        password=form_data.password
    )
    usecase = LoginUsecaseInteractor(input)
    presenter = LoginPresenter(usecase.handle())
    viewModel = presenter.api()

    if not viewModel['is_success']:
        if viewModel['error'].type == UnauthorizedError.TYPE_CODE:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail=viewModel['error'].message,
                headers={'WWW-Authenticate': 'Bearer'}
            )

    auth.set_access_token_cookie(
        response, viewModel['access_token'], viewModel['expires'])
    return {'token': viewModel['identified_token']}


@router.post('/logout')
async def logout(response: Response):
    response.delete_cookie('access_token')
    return {'isLoggedOut': True}

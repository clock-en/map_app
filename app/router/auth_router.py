from fastapi import APIRouter, Depends, Response, HTTPException, status
from app.core.sqlalchemy.schema import auth_schema
from app.usecase.auth import SignInUsecaseInput, SignInUsecaseInteractor
from app.adapter.presenter.auth import SignInPresenter
from app.domain.value_object.error.unauthorized_error import UnauthorizedError
from app.utility import auth

router = APIRouter(prefix='/api/auth', tags=['auth'])


@router.post('/signin')
async def signin(
    response: Response,
    form_data: auth_schema.OAuth2EmailPasswordRequestForm = Depends(),
):
    input = SignInUsecaseInput(
        email=form_data.username,
        password=form_data.password
    )
    usecase = SignInUsecaseInteractor(input)
    presenter = SignInPresenter(usecase.handle())
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


@router.post('/signout')
async def signout(response: Response):
    response.delete_cookie('access_token')
    return {'isLoggedOut': True}

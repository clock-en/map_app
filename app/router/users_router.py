from fastapi import APIRouter, Body, Path, Depends, HTTPException, status
from app.schema import users_schema
from app.usecase.user import (
    CreateUserUsecaseInput,
    CreateUserUsecaseInteractor,
    FetchUserUsecaseInput,
    FetchUserUsecaseInteractor
)
from app.adapter.presenter.user import UsersCreatePresenter, UsersIdPresenter
from app.domain.value_object.error.unprocessable_entity_error import (
    UnprocessableEntityError)
from app.domain.value_object.error.notfound_error import NotFoundError
from app.utility import auth

router = APIRouter(prefix='/api/users', tags=['users'])


@router.post(
    '',
    response_model=users_schema.User,
    status_code=status.HTTP_201_CREATED,
    dependencies=[Depends(auth.validate_content_type)]
)
async def create_user(
    user: users_schema.UserCreate = Body(embed=False)
):
    input = CreateUserUsecaseInput(
        name=user.name,
        email=user.email,
        password=user.password
    )
    usecase = CreateUserUsecaseInteractor(input)
    presenter = UsersCreatePresenter(usecase.handle())
    viewModel = presenter.api()

    if not viewModel['is_success']:
        if viewModel['error'].type == UnprocessableEntityError.TYPE_CODE:
            raise HTTPException(
                status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
                detail=[{
                    'loc': ['body', viewModel['error'].field],
                    'msg': viewModel['error'].message,
                    'type': 'value_error.' + viewModel['error'].field
                }])
    return viewModel['user']


@router.get(
    '/me',
    response_model=users_schema.User,
    status_code=status.HTTP_200_OK,
)
async def get_user_me(
    current_user: users_schema.User = Depends(auth.authorize_user)
):
    return current_user


@router.get(
    '/{id}',
    response_model=users_schema.User,
    status_code=status.HTTP_200_OK,
    dependencies=[Depends(auth.authorize_user)]
)
async def get_user(
    id: int = Path(ge=1),
):
    input = FetchUserUsecaseInput(id)
    usecase = FetchUserUsecaseInteractor(input)
    presenter = UsersIdPresenter(usecase.handle())
    viewModel = presenter.api()
    if not viewModel['is_success']:
        if viewModel['error'].type == NotFoundError.TYPE_CODE:
            raise HTTPException(
                status_code=404, detail=viewModel['error'].message)
    return viewModel['user']

from fastapi import (
    APIRouter,
    Body,
    Path,
    Depends,
    HTTPException,
    status)
from sqlalchemy.orm import Session
from app.schema import users_schema
from app.core.sqlalchemy.database import get_db
from app.crud import users_crud
from app.utility import auth

router = APIRouter(prefix='/api/users', tags=['users'])


@router.post(
    '',
    response_model=users_schema.User,
    status_code=status.HTTP_201_CREATED,
    dependencies=[Depends(auth.validate_content_type),
                  Depends(auth.authorize_with_x_token)]
)
async def create_user(
    user: users_schema.UserCreate = Body(embed=False),
    db: Session = Depends(get_db),
):
    db_user = users_crud.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail=[{
                'loc': ['body', 'email'],
                'msg': 'Email already registered',
                'type': 'value_error.email'
            }])
    return users_crud.create_user(db=db, user=user)


@router.get(
    '/me',
    response_model=users_schema.User,
    status_code=status.HTTP_200_OK,
)
async def read_users_me(
    current_user: users_schema.User = Depends(auth.authorize_user)
):
    return current_user


@router.get(
    '/{user_id}',
    response_model=users_schema.User,
    status_code=status.HTTP_200_OK,
    dependencies=[Depends(auth.authorize_user)]
)
async def read_user(
    user_id: int = Path(ge=1),
    db: Session = Depends(get_db),
):
    db_user = users_crud.get_user_by_id(db, id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail='User not found')
    return db_user

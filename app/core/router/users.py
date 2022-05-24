from fastapi import (
    APIRouter,
    Body,
    Path,
    Depends,
    HTTPException,
    status)
from sqlalchemy.orm import Session
from app.core.orm import crud, schemas
from app.core.orm.database import get_db

router = APIRouter(prefix='/api/users', tags=['users'])


@router.post(
    '',
    response_model=schemas.User,
    status_code=status.HTTP_201_CREATED
)
async def create_user(
    user: schemas.UserCreate = Body(embed=False),
    db: Session = Depends(get_db)
):
    db_user = crud.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Email already registered")
    return crud.create_user(db=db, user=user)


@router.get(
    '/{user_id}',
    response_model=schemas.User,
    status_code=status.HTTP_200_OK
)
async def read_user(user_id: int = Path(ge=1), db: Session = Depends(get_db)):
    db_user = crud.get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user

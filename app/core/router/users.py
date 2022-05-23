from fastapi import APIRouter, Body, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.core.orm import crud, schemas
from app.core.orm.database import get_db

router = APIRouter(prefix='/api/user', tags=['user'])


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

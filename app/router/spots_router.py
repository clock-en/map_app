from typing import List
from fastapi import APIRouter, Body, Path, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.schema import spots_schema
from app.crud import spots_crud
from app.database import get_db
from app.utility import auth

router = APIRouter(prefix='/api/spots', tags=['spots'])


@router.post(
    '',
    response_model=spots_schema.Spot,
    status_code=status.HTTP_201_CREATED,
    dependencies=[Depends(auth.validate_content_type),
                  Depends(auth.authorize_with_x_token)]
)
async def create_spot(
    spot: spots_schema.SpotCreate = Body(embed=False),
    db: Session = Depends(get_db),
):
    db_spot = spots_crud.get_registered_spot(
        db, spot.name, spot.latitude, spot.longitude)
    if db_spot:
        if db_spot.name == spot.name:
            raise HTTPException(
                status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
                detail=[{
                    'loc': ['body', 'name'],
                    'msg': 'Name already registered',
                    'type': 'value_error.name'
                }])
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail=[{
                'loc': ['body', 'location'],
                'msg': 'Location already registered',
                'type': 'value_error.location'
            }])
    return spots_crud.create_spot(db=db, spot=spot)


@router.get(
    '',
    response_model=List[spots_schema.Spot],
    status_code=status.HTTP_201_CREATED,
    dependencies=[Depends(auth.authorize_user)]
)
async def fetch_spots(
    db: Session = Depends(get_db),
):
    return spots_crud.get_spots(db=db)


@router.get(
    '/{spot_id}',
    response_model=spots_schema.Spot,
    status_code=status.HTTP_200_OK,
    dependencies=[Depends(auth.authorize_user)]
)
async def read_user(
    spot_id: int = Path(ge=1),
    db: Session = Depends(get_db),
):
    db_spot = spots_crud.get_spot_by_id(db, id=spot_id)
    if db_spot is None:
        raise HTTPException(status_code=404, detail='Spot not found')
    return db_spot

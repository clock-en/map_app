from typing import List
from fastapi import APIRouter, Body, Depends, HTTPException, status
from app.schema import spots_schema
from app.adapter.presenter.spots.spots_create_presenter import (
    SpotsCreatePresenter)
from app.adapter.presenter.spots.spots_index_presenter import (
    SpotsIndexPresenter)
from app.usecase.spot.create.create_spot_usecase_input import (
    CreateSpotUsecaseInput)
from app.usecase.spot.create.create_spot_usecase_interactor import (
    CreateSpotUsecaseInteractor)
from app.usecase.spot.fetch_all.fetch_all_spots_usecase_interactor import (
    FetchAllSpotsUsecaseInteractor)
from app.domain.value_object.error.unprocessable_entity_error import (
    UnprocessableEntityError)
from app.utility import auth

router = APIRouter(prefix='/api/spots', tags=['spots'])


@router.get(
    '',
    response_model=List[spots_schema.Spot],
    status_code=status.HTTP_201_CREATED,
    dependencies=[Depends(auth.authorize_user)]
)
async def fetch_spots():
    usecase = FetchAllSpotsUsecaseInteractor()
    presenter = SpotsIndexPresenter(usecase.handle())
    viewModel = presenter.api()
    return viewModel['spots']


@router.post(
    '',
    response_model=spots_schema.Spot,
    status_code=status.HTTP_201_CREATED,
    dependencies=[Depends(auth.validate_content_type),
                  Depends(auth.authorize_with_x_token)]
)
async def create_spot(
    spot: spots_schema.SpotCreate = Body(embed=False),
):
    input = CreateSpotUsecaseInput(
        name=spot.name,
        latitude=spot.latitude,
        longitude=spot.longitude,
        user_id=spot.user_id
    )
    usecase = CreateSpotUsecaseInteractor(input)
    presenter = SpotsCreatePresenter(usecase.handle())
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
    return viewModel['spot']


"""
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
"""

from typing import List
from fastapi import APIRouter, Body, Path, Depends, HTTPException, status
from app.core.sqlalchemy.schema import spots_schema
from app.adapter.presenter.spots import (
    SpotsCreatePresenter,
    SpotsIndexPresenter,
    SpotsIdPresenter
)
from app.usecase.spot import (
    CreateSpotUsecaseInput,
    CreateSpotUsecaseInteractor,
    FetchSpotsUsecaseInteractor,
    FetchSpotUsecaseInput,
    FetchSpotUsecaseInteractor
)
from app.domain.value_object.error.unprocessable_entity_error import (
    UnprocessableEntityError)
from app.domain.value_object.error.notfound_error import NotFoundError
from app.utility import auth

router = APIRouter(prefix='/api/spots', tags=['spots'])


@router.get(
    '',
    response_model=List[spots_schema.Spot],
    status_code=status.HTTP_201_CREATED,
    dependencies=[Depends(auth.authorize_user)]
)
async def get_spots():
    usecase = FetchSpotsUsecaseInteractor()
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


@router.get(
    '/{id}',
    response_model=spots_schema.Spot,
    status_code=status.HTTP_200_OK,
    dependencies=[Depends(auth.authorize_user)]
)
async def get_spot(
    id: int = Path(ge=1),
):
    input = FetchSpotUsecaseInput(id)
    usecase = FetchSpotUsecaseInteractor(input)
    presenter = SpotsIdPresenter(usecase.handle())
    viewModel = presenter.api()
    if not viewModel['is_success']:
        if viewModel['error'].type == NotFoundError.TYPE_CODE:
            raise HTTPException(
                status_code=404, detail=viewModel['error'].message)
    return viewModel['spot']

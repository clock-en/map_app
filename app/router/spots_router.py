from typing import List
from fastapi import APIRouter, Body, Path, Depends, HTTPException, status
from app.core.sqlalchemy.schema import spots_schema
from app.core.sqlalchemy.schema import users_schema
from app.adapter.presenter.spots import (
    SpotsCreatePresenter,
    SpotsModifyPresenter,
    SpotsIndexPresenter,
    SpotsIdPresenter
)
from app.usecase.spot import (
    CreateSpotUsecaseInput,
    CreateSpotUsecaseInteractor,
    ModifySpotUsecaseInput,
    ModifySpotUsecaseInteractor,
    FetchSpotsUsecaseInput,
    FetchSpotsUsecaseInteractor,
    FetchSpotUsecaseInput,
    FetchSpotUsecaseInteractor,
)
from app.domain.value_object.error.unprocessable_entity_error import (
    UnprocessableEntityError)
from app.domain.value_object.error.bad_request_error import BadRequestError
from app.domain.value_object.error.conflict_error import ConflictError
from app.domain.value_object.error.notfound_error import NotFoundError
from app.utility import auth

router = APIRouter(prefix='/api/spots', tags=['spots'])


@router.get(
    '',
    response_model=List[spots_schema.Spot],
    status_code=status.HTTP_201_CREATED,
)
async def get_spots(
    current_user: users_schema.User = Depends(auth.authorize_user),
    is_own: bool = None,
):
    input = FetchSpotsUsecaseInput(user_id=current_user.id, is_own=is_own)
    usecase = FetchSpotsUsecaseInteractor(input)
    presenter = SpotsIndexPresenter(usecase.handle())
    viewModel = presenter.api()
    return viewModel['spots']


@router.post(
    '',
    response_model=spots_schema.Spot,
    status_code=status.HTTP_201_CREATED,
    dependencies=[Depends(auth.validate_content_type)]
)
async def create_spot(
    spot: spots_schema.SpotCreate = Body(embed=False),
    current_user: users_schema.User = Depends(auth.authorize_with_x_token)
):
    input = CreateSpotUsecaseInput(
        name=spot.name,
        latitude=spot.latitude,
        description=spot.description,
        longitude=spot.longitude,
        user_id=current_user.id
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
)
async def get_spot(
    id: int = Path(ge=1),
    current_user: users_schema.User = Depends(auth.authorize_user),
    is_own: bool = None
):
    input = FetchSpotUsecaseInput(
        id=id,
        user_id=current_user.id,
        is_own=is_own
    )
    usecase = FetchSpotUsecaseInteractor(input)
    presenter = SpotsIdPresenter(usecase.handle())
    viewModel = presenter.api()
    if not viewModel['is_success']:
        if viewModel['error'].type == NotFoundError.TYPE_CODE:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=viewModel['error'].message
            )
        if viewModel['error'].type == BadRequestError.TYPE_CODE:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=viewModel['error'].message
            )
    return viewModel['spot']


@router.put(
    '/{id}',
    response_model=spots_schema.Spot,
    status_code=status.HTTP_200_OK,
    dependencies=[Depends(auth.validate_content_type)]
)
async def modify_spot(
    spot: spots_schema.SpotModify = Body(embed=False),
    current_user: users_schema.User = Depends(auth.authorize_with_x_token)
):
    input = ModifySpotUsecaseInput(
        id=spot.id,
        name=spot.name,
        description=spot.description,
        latitude=spot.latitude,
        longitude=spot.longitude,
        user_id=current_user.id,
        updated_at=spot.updated_at,
    )
    usecase = ModifySpotUsecaseInteractor(input)
    presenter = SpotsModifyPresenter(usecase.handle())
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
        if viewModel['error'].type == BadRequestError.TYPE_CODE:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=viewModel['error'].message
            )
        if viewModel['error'].type == ConflictError.TYPE_CODE:
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail=viewModel['error'].message
            )
    return viewModel['spot']

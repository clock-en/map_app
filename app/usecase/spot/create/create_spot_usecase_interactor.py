from app.adapter.repository.spot_repository import SpotRepository
from app.adapter.query_service.spot_query_service import SpotQueryService
from app.domain.value_object.spot.new_spot import NewSpot
from app.domain.value_object.error.unprocessable_entity_error import (
    UnprocessableEntityError)
from .create_spot_usecase_input import CreateSpotUsecaseInput
from .create_spot_usecase_output import CreateSpotUsecaseOutput


class CreateSpotUsecaseInteractor(object):
    __input: CreateSpotUsecaseInput
    __repository: SpotRepository
    __query_service: SpotQueryService

    def __init__(self, input: CreateSpotUsecaseInput) -> None:
        self.__input = input
        self.__repository = SpotRepository()
        self.__query_service = SpotQueryService()

    def handle(self) -> CreateSpotUsecaseOutput:
        db_spot = self.__query_service.fetch_registered_spot(
            name=self.__input.name,
            latitude=self.__input.latitude,
            longitude=self.__input.longitude
        )
        if db_spot:
            if db_spot.name.value == self.__input.name.value:
                return CreateSpotUsecaseOutput(
                    is_success=False,
                    error=UnprocessableEntityError(
                        field='name', message='入力されたスポット名はすでに登録されています')
                )
            return CreateSpotUsecaseOutput(
                is_success=False,
                error=UnprocessableEntityError(
                    field='location', message='入力されたロケーションはすでに登録されています')
            )

        new_spot = NewSpot(
            name=self.__input.name.value,
            description=self.__input.description.value,
            latitude=self.__input.latitude.value,
            longitude=self.__input.longitude.value,
            user_id=self.__input.user_id.value
        )
        spot = self.__repository.create(new_spot)
        return CreateSpotUsecaseOutput(is_success=True, spot=spot)

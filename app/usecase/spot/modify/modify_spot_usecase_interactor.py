from app.adapter.repository.spot_repository import SpotRepository
from app.adapter.query_service.spot_query_service import SpotQueryService
from app.domain.value_object.error.unprocessable_entity_error import (
    UnprocessableEntityError)
from app.domain.value_object.error.bad_request_error import BadRequestError
from app.domain.value_object.error.conflict_error import ConflictError
from .modify_spot_usecase_input import ModifySpotUsecaseInput
from .modify_spot_usecase_output import ModifySpotUsecaseOutput


class ModifySpotUsecaseInteractor(object):
    __input: ModifySpotUsecaseInput
    __repository: SpotRepository
    __query_service: SpotQueryService

    def __init__(self, input: ModifySpotUsecaseInput) -> None:
        self.__input = input
        self.__repository = SpotRepository()
        self.__query_service = SpotQueryService()

    def handle(self) -> ModifySpotUsecaseOutput:
        registered_spot = self.__query_service.fetch_registered_spot(
            name=self.__input.name,
            latitude=self.__input.latitude,
            longitude=self.__input.longitude
        )
        if registered_spot:
            if registered_spot.name.value == self.__input.name.value:
                return ModifySpotUsecaseOutput(
                    is_success=False,
                    error=UnprocessableEntityError(
                        field='name', message='入力されたスポット名はすでに登録されています')
                )
            return ModifySpotUsecaseOutput(
                is_success=False,
                error=UnprocessableEntityError(
                    field='location', message='入力されたロケーションはすでに登録されています')
            )

        db_spot = self.__query_service.fetch_my_registered_spot_by_ids(
            id=self.__input.id,
            user_id=self.__input.user_id,
        )
        if db_spot is None:
            return ModifySpotUsecaseOutput(
                is_success=False,
                error=BadRequestError('不正な値が送信されています。ページを更新し、操作をやり直してください')
            )
        if db_spot.updated_at.value != self.__input.updated_at.value:
            return ModifySpotUsecaseOutput(
                is_success=False,
                error=ConflictError(
                    '対象のユーザー情報はすでに別の操作で変更されています。ページを更新し、操作をやり直してください')
            )

        spot = self.__repository.modify(
            id=self.__input.id.value,
            name=self.__input.name.value,
            description=self.__input.description.value,
            latitude=self.__input.latitude.value,
            longitude=self.__input.longitude.value,
        )
        return ModifySpotUsecaseOutput(is_success=True, spot=spot)

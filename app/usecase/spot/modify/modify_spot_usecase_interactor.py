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
        registered_spots = self.__query_service.fetch_registered_spots(
            name=self.__input.name,
            latitude=self.__input.latitude,
            longitude=self.__input.longitude
        )

        for registered_spot in registered_spots:
            if (registered_spot and
                    not registered_spot.id.__eq__(self.__input.id)):
                if registered_spot.name.__eq__(self.__input.name):
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
        if not db_spot.updated_at.__eq__(self.__input.updated_at):
            return ModifySpotUsecaseOutput(
                is_success=False,
                error=ConflictError(
                    '対象のユーザー情報はすでに別の操作で変更されています。ページを更新し、操作をやり直してください')
            )

        spot = self.__repository.modify(
            id=self.__input.id,
            name=self.__input.name,
            description=self.__input.description,
            latitude=self.__input.latitude,
            longitude=self.__input.longitude,
        )
        return ModifySpotUsecaseOutput(is_success=True, spot=spot)

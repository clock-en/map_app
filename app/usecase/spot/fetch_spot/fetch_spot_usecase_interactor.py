from app.adapter.query_service.spot_query_service import SpotQueryService
from app.domain.value_object.error.bad_request_error import BadRequestError
from app.domain.value_object.error.notfound_error import NotFoundError
from .fetch_spot_usecase_input import FetchSpotUsecaseInput
from .fetch_spot_usecase_output import FetchSpotUsecaseOutput


class FetchSpotUsecaseInteractor(object):
    __input: FetchSpotUsecaseInput
    __query_service: SpotQueryService

    def __init__(self, input: FetchSpotUsecaseInput) -> None:
        self.__input = input
        self.__query_service = SpotQueryService()

    def handle(self) -> FetchSpotUsecaseOutput:
        spot = self.__query_service.fetch_spot_by_id(self.__input.id)
        if (self.__input.editable and
                not spot.user_id.__eq__(self.__input.user_id)):
            return FetchSpotUsecaseOutput(
                is_success=False,
                error=BadRequestError('不正な値が送信されました。ページを更新し、操作をやり直してください。')
            )
        if spot is None:
            return FetchSpotUsecaseOutput(
                is_success=False,
                error=NotFoundError('スポットは見つかりませんでした')
            )
        return FetchSpotUsecaseOutput(is_success=True, spot=spot)

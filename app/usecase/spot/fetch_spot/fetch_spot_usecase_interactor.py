from app.adapter.query_service.spot_query_service import SpotQueryService
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
        if spot is None:
            return FetchSpotUsecaseOutput(
                is_success=False,
                error=NotFoundError('スポットは見つかりませんでした')
            )
        return FetchSpotUsecaseOutput(is_success=True, spot=spot)

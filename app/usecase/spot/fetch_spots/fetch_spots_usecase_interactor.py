from typing import Union, List
from app.adapter.query_service.spot_query_service import SpotQueryService
from app.domain.entity.spot import Spot
from .fetch_spots_usecase_input import FetchSpotsUsecaseInput
from .fetch_spots_usecase_output import FetchSpotsUsecaseOutput


class FetchSpotsUsecaseInteractor(object):
    __input: FetchSpotsUsecaseInput
    __query_service: SpotQueryService

    def __init__(self, input: FetchSpotsUsecaseInput) -> None:
        self.__input = input
        self.__query_service = SpotQueryService()

    def handle(self) -> FetchSpotsUsecaseOutput:
        spots = self.__fetch_spots()

        if spots is None or not spots:
            return FetchSpotsUsecaseOutput(is_success=True, spots=[])
        return FetchSpotsUsecaseOutput(is_success=True, spots=spots)

    def __fetch_spots(self) -> Union[List[Spot], None]:
        if (self.__input.user_id is not None):
            return self.__query_service.fetch_spot_by_user_id(
                self.__input.user_id)
        return self.__query_service.fetch_all_spots()

from app.adapter.query_service.spot_query_service import SpotQueryService
from .fetch_spots_usecase_output import FetchSpotsUsecaseOutput


class FetchSpotsUsecaseInteractor(object):
    __query_service: SpotQueryService

    def __init__(self) -> None:
        self.__query_service = SpotQueryService()

    def handle(self) -> FetchSpotsUsecaseOutput:
        spots = self.__query_service.fetch_all_spots()
        if spots is None or not spots:
            return FetchSpotsUsecaseOutput(is_success=True, spots=[])
        return FetchSpotsUsecaseOutput(is_success=True, spots=spots)

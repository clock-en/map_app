from typing import List
from app.core.sqlalchemy.data_model.spot_data_model import SpotDataModel
from app.usecase.spot.fetch_all.fetch_all_spots_usecase_output import (
    FetchAllSpotsUsecaseOutput)
from app.domain.entity.spot import Spot


class SpotsIndexViewModel(object):
    __output: FetchAllSpotsUsecaseOutput

    def __init__(self, output: FetchAllSpotsUsecaseOutput) -> None:
        self.__output = output

    def convertToFastApi(self) -> FetchAllSpotsUsecaseOutput:
        return {
            'is_success': self.__output.is_success,
            'error': self.__output.error,
            'spots': self.__create_spot_list()
        }

    def __create_spot_list(self) -> List[SpotDataModel]:
        if self.__output.spots is None:
            return None
        return list(map(self.__create_spot_data_model, self.__output.spots))

    def __create_spot_data_model(self, spot: Spot):
        return SpotDataModel(
            id=spot.id.value,
            name=spot.name.value,
            latitude=spot.latitude.value,
            longitude=spot.longitude.value,
            user_id=spot.user_id.value
        )

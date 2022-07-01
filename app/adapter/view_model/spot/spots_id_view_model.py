from typing import Union
from app.core.sqlalchemy.data_model.spot_data_model import SpotDataModel
from app.usecase.spot.fetch_spot.fetch_spot_usecase_output import (
    FetchSpotUsecaseOutput)


class SpotsIdViewModel(object):
    __output: FetchSpotUsecaseOutput

    def __init__(self, output: FetchSpotUsecaseOutput) -> None:
        self.__output = output

    def convertToFastApi(self) -> FetchSpotUsecaseOutput:
        return {
            'is_success': self.__output.is_success,
            'error': self.__output.error,
            'spot': self.__create_spot_with_comments_data_model()
        }

    def __create_spot_with_comments_data_model(
        self
    ) -> Union[SpotDataModel, None]:
        if self.__output.spot is None:
            return None

        return SpotDataModel(
            id=self.__output.spot.id.value,
            name=self.__output.spot.name.value,
            description=self.__output.spot.description.value,
            latitude=self.__output.spot.latitude.value,
            longitude=self.__output.spot.longitude.value,
            user_id=self.__output.spot.user_id.value,
            created_at=self.__output.spot.created_at.value,
            updated_at=self.__output.spot.updated_at.value
        )

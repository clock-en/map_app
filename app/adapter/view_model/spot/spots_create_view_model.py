from app.core.sqlalchemy.data_model.spot_data_model import SpotDataModel
from app.usecase.spot.create.create_spot_usecase_output import (
    CreateSpotUsecaseOutput)


class SpotsCreateViewModel(object):
    __output: CreateSpotUsecaseOutput

    def __init__(self, output: CreateSpotUsecaseOutput) -> None:
        self.__output = output

    def convertToFastApi(self) -> CreateSpotUsecaseOutput:
        return {
            'is_success': self.__output.is_success,
            'error': self.__output.error,
            'spot': self.__create_spot_data_model()
        }

    def __create_spot_data_model(self):
        if self.__output.spot is None:
            return None
        return SpotDataModel(
            id=self.__output.spot.id.value,
            name=self.__output.spot.name.value,
            description=self.__output.spot.description.value,
            latitude=self.__output.spot.latitude.value,
            longitude=self.__output.spot.longitude.value,
            user_id=self.__output.spot.user_id.value
        )

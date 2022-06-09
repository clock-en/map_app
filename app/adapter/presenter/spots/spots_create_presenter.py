from app.adapter.view_model.spot.spots_create_view_model import (
    SpotsCreateViewModel)
from app.usecase.spot.create.create_spot_usecase_output import (
    CreateSpotUsecaseOutput)


class SpotsCreatePresenter(object):
    __output: CreateSpotUsecaseOutput

    def __init__(self, output: CreateSpotUsecaseOutput) -> None:
        self.__output = output

    def api(self):
        viewModel = SpotsCreateViewModel(self.__output)
        return viewModel.convertToFastApi()

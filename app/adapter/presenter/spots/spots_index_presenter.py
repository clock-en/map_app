from app.adapter.view_model.spot.spots_index_view_model import (
    SpotsIndexViewModel)
from app.usecase.spot.create.create_spot_usecase_output import (
    CreateSpotUsecaseOutput)


class SpotsIndexPresenter(object):
    __output: CreateSpotUsecaseOutput

    def __init__(self, output: CreateSpotUsecaseOutput) -> None:
        self.__output = output

    def api(self):
        viewModel = SpotsIndexViewModel(self.__output)
        return viewModel.convertToFastApi()

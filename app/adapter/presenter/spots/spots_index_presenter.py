from app.adapter.view_model.spot.spots_index_view_model import (
    SpotsIndexViewModel)
from app.usecase.spot import (
    FetchSpotsUsecaseOutput)


class SpotsIndexPresenter(object):
    __output: FetchSpotsUsecaseOutput

    def __init__(self, output: FetchSpotsUsecaseOutput) -> None:
        self.__output = output

    def api(self):
        viewModel = SpotsIndexViewModel(self.__output)
        return viewModel.convertToFastApi()

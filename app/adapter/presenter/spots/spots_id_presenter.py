from app.adapter.view_model.spot.spots_id_view_model import (
    SpotsIdViewModel)
from app.usecase.spot.fetch_spot.fetch_spot_usecase_output import (
    FetchSpotUsecaseOutput)


class SpotsIdPresenter(object):
    __output: FetchSpotUsecaseOutput

    def __init__(self, output: FetchSpotUsecaseOutput) -> None:
        self.__output = output

    def api(self):
        viewModel = SpotsIdViewModel(self.__output)
        return viewModel.convertToFastApi()

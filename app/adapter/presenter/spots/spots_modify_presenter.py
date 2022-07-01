from app.adapter.view_model.spot.spots_modify_view_model import (
    SpotsModifyViewModel)
from app.usecase.spot.modify.modify_spot_usecase_output import (
    ModifySpotUsecaseOutput)


class SpotsModifyPresenter(object):
    __output: ModifySpotUsecaseOutput

    def __init__(self, output: ModifySpotUsecaseOutput) -> None:
        self.__output = output

    def api(self):
        viewModel = SpotsModifyViewModel(self.__output)
        return viewModel.convertToFastApi()

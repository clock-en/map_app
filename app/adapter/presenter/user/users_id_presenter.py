from app.adapter.view_model.user.users_id_view_model import (
    UsersIdViewModel)
from app.usecase.spot.fetch_spot.fetch_spot_usecase_output import (
    FetchSpotUsecaseOutput)


class UsersIdPresenter(object):
    __output: FetchSpotUsecaseOutput

    def __init__(self, output: FetchSpotUsecaseOutput) -> None:
        self.__output = output

    def api(self):
        viewModel = UsersIdViewModel(self.__output)
        return viewModel.convertToFastApi()

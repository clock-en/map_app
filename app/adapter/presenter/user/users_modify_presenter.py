from app.adapter.view_model.user.users_modify_view_model import (
    UsersModifyViewModel)
from app.usecase.user import ModifyUserUsecaseOutput


class UsersModifyPresenter(object):
    __output: ModifyUserUsecaseOutput

    def __init__(self, output: ModifyUserUsecaseOutput) -> None:
        self.__output = output

    def api(self):
        viewModel = UsersModifyViewModel(self.__output)
        return viewModel.convertToFastApi()

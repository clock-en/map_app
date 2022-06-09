from app.adapter.view_model.user.users_create_view_model import (
    UsersCreateViewModel)
from app.usecase.user import CreateUserUsecaseOutput


class UsersCreatePresenter(object):
    __output: CreateUserUsecaseOutput

    def __init__(self, output: CreateUserUsecaseOutput) -> None:
        self.__output = output

    def api(self):
        viewModel = UsersCreateViewModel(self.__output)
        return viewModel.convertToFastApi()

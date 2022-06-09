from app.adapter.view_model.auth.login_view_model import (
    LoginViewModel)
from app.usecase.auth import LoginUsecaseOutput


class LoginPresenter(object):
    __output: LoginUsecaseOutput

    def __init__(self, output: LoginUsecaseOutput) -> None:
        self.__output = output

    def api(self):
        viewModel = LoginViewModel(self.__output)
        return viewModel.convertToFastApi()

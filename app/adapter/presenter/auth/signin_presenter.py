from app.adapter.view_model.auth.signin_view_model import (
    SignInViewModel)
from app.usecase.auth import SignInUsecaseOutput


class SignInPresenter(object):
    __output: SignInUsecaseOutput

    def __init__(self, output: SignInUsecaseOutput) -> None:
        self.__output = output

    def api(self):
        viewModel = SignInViewModel(self.__output)
        return viewModel.convertToFastApi()

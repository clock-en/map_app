from app.usecase.auth import LoginUsecaseOutput


class LoginViewModel(object):
    __output: LoginUsecaseOutput

    def __init__(self, output: LoginUsecaseOutput) -> None:
        self.__output = output

    def convertToFastApi(self):
        return {
            'is_success': self.__output.is_success,
            'error': self.__output.error,
            'access_token': self.__output.access_token,
            'expires': self.__output.expires,
            'identified_token': self.__output.identified_token
        }

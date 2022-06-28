from app.usecase.auth import SignInUsecaseOutput


class SignInViewModel(object):
    __output: SignInUsecaseOutput

    def __init__(self, output: SignInUsecaseOutput) -> None:
        self.__output = output

    def convertToFastApi(self):
        return {
            'is_success': self.__output.is_success,
            'error': self.__output.error,
            'access_token': self.__output.access_token,
            'expires': self.__output.expires,
            'identified_token': self.__output.identified_token
        }

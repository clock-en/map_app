from app.core.sqlalchemy.data_model.user_data_model import UserDataModel
from app.usecase.user import CreateUserUsecaseOutput


class UsersCreateViewModel(object):
    __output: CreateUserUsecaseOutput

    def __init__(self, output: CreateUserUsecaseOutput) -> None:
        self.__output = output

    def convertToFastApi(self):
        return {
            'is_success': self.__output.is_success,
            'error': self.__output.error,
            'user': self.__create_user_data_model()
        }

    def __create_user_data_model(self):
        if self.__output.user is None:
            return None
        return UserDataModel(
            id=self.__output.user.id.value,
            name=self.__output.user.name.value,
            email=self.__output.user.email.value,
            password=self.__output.user.password,
            created_at=self.__output.user.created_at.value,
            updated_at=self.__output.user.updated_at.value
        )

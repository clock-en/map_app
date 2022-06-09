from app.adapter.repository.user_repository import UserRepository
from app.adapter.query_service.user_query_service import UserQueryService
from app.domain.value_object.user.new_user import NewUser
from app.domain.value_object.error.unprocessable_entity_error import (
    UnprocessableEntityError)
from .create_user_usecase_input import CreateUserUsecaseInput
from .create_user_usecase_output import CreateUserUsecaseOutput


class CreateUserUsecaseInteractor(object):
    __input: CreateUserUsecaseInput
    __repository: UserRepository
    __query_service: UserQueryService

    def __init__(self, input: CreateUserUsecaseInput) -> None:
        self.__input = input
        self.__repository = UserRepository()
        self.__query_service = UserQueryService()

    def handle(self) -> CreateUserUsecaseOutput:
        db_user = self.__query_service.fetch_user_by_email(self.__input.email)
        if db_user:
            return CreateUserUsecaseOutput(
                is_success=False,
                error=UnprocessableEntityError(
                    field='email', message='Email already registered')
            )

        new_user = NewUser(
            name=self.__input.name.value,
            email=self.__input.email.value,
            password=self.__input.password.value
        )
        user = self.__repository.create(new_user)
        return CreateUserUsecaseOutput(is_success=True, user=user)

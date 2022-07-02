from app.adapter.repository.user_repository import UserRepository
from app.adapter.query_service.user_query_service import UserQueryService
from app.domain.value_object.error.conflict_error import ConflictError
from app.domain.value_object.error.unprocessable_entity_error import (
    UnprocessableEntityError)
from .modify_user_usecase_input import ModifyUserUsecaseInput
from .modify_user_usecase_output import ModifyUserUsecaseOutput


class ModifyUserUsecaseInteractor(object):
    __input: ModifyUserUsecaseInput
    __repository: UserRepository
    __query_service: UserQueryService

    def __init__(self, input: ModifyUserUsecaseInput) -> None:
        self.__input = input
        self.__repository = UserRepository()
        self.__query_service = UserQueryService()

    def handle(self) -> ModifyUserUsecaseOutput:
        registered_user = self.__query_service.fetch_user_by_email(
            self.__input.email)
        if (registered_user and
                not registered_user.id.__eq__(self.__input.id)):
            return ModifyUserUsecaseOutput(
                is_success=False,
                error=UnprocessableEntityError(
                    field='email', message='入力されたメールアドレスはすでに登録されています')
            )
        db_user = self.__query_service.fetch_user_by_id(self.__input.id)
        if not db_user.updated_at.__eq__(self.__input.updated_at):
            return ModifyUserUsecaseOutput(
                is_success=False,
                error=ConflictError(
                    '対象のユーザー情報はすでに別の操作で変更されています。ページを更新し、操作をやり直してください。')
            )

        user = self.__repository.modify(
            id=self.__input.id,
            name=self.__input.name,
            email=self.__input.email
        )
        return ModifyUserUsecaseOutput(is_success=True, user=user)

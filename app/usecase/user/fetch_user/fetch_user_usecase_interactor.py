from app.adapter.query_service.user_query_service import UserQueryService
from app.domain.value_object.error.notfound_error import NotFoundError
from .fetch_user_usecase_input import FetchUserUsecaseInput
from .fetch_user_usecase_output import FetchUserUsecaseOutput


class FetchUserUsecaseInteractor(object):
    __input: FetchUserUsecaseInput
    __query_service: UserQueryService

    def __init__(self, input: FetchUserUsecaseInput) -> None:
        self.__input = input
        self.__query_service = UserQueryService()

    def handle(self) -> FetchUserUsecaseOutput:
        user = self.__query_service.fetch_user_by_id(self.__input.id)
        if user is None:
            return FetchUserUsecaseOutput(
                is_success=False,
                error=NotFoundError('User not found.')
            )
        return FetchUserUsecaseOutput(is_success=True, user=user)

from app.adapter.query_service.user_query_service import UserQueryService
from app.domain.value_object.error.unauthorized_error import UnauthorizedError
from app.utility import auth
from .signin_usecase_input import SignInUsecaseInput
from .signin_usecase_output import SignInUsecaseOutput


class SignInUsecaseInteractor(object):
    __input: SignInUsecaseInput
    __query_service: UserQueryService

    def __init__(self, input: SignInUsecaseInput) -> None:
        self.__input = input
        self.__query_service = UserQueryService()

    def handle(self) -> SignInUsecaseOutput:
        user = self.__query_service.fetch_user_by_email(self.__input.email)
        if ((user is None) or
                (not user.password.verify(self.__input.password.value))):
            return SignInUsecaseOutput(
                is_success=False,
                error=UnauthorizedError('ユーザー名またはパスワードが誤っています')
            )

        # JWT発行
        expires = auth.create_access_token_expires()
        access_token = auth.create_access_token(user.id.value, expires)

        # リクエスト時のカスタムヘッダー用にユーザーごとに固定となるトークンを発行する
        identified_token = auth.create_identified_token(user.id.value)
        return SignInUsecaseOutput(
            is_success=True,
            access_token=access_token,
            identified_token=identified_token,
            expires=expires
        )

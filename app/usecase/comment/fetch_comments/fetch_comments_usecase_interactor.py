from typing import Union, List
from app.adapter.query_service.comment_query_service import CommentQueryService
from app.domain.entity.comment import CommentWithUser
from .fetch_comments_usecase_input import FetchCommentsUsecaseInput
from .fetch_comments_usecase_output import FetchCommentsUsecaseOutput


class FetchCommentsUsecaseInteractor(object):
    __input: FetchCommentsUsecaseInput
    __query_service: CommentQueryService

    def __init__(self, input: FetchCommentsUsecaseInput) -> None:
        self.__input = input
        self.__query_service = CommentQueryService()

    def handle(self) -> FetchCommentsUsecaseOutput:
        comments = self.__fetch_comments()

        if comments is None or not comments:
            return FetchCommentsUsecaseOutput(is_success=True, comments=[])
        return FetchCommentsUsecaseOutput(is_success=True, comments=comments)

    def __fetch_comments(self) -> Union[List[CommentWithUser], None]:
        return self.__query_service.fetch_comments_by_spot_id(
            self.__input.spot_id)

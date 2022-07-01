from app.adapter.repository.comment_repository import CommentRepository
from app.domain.value_object.comment.new_comment import NewComment
from .create_comment_usecase_input import CreateCommentUsecaseInput
from .create_comment_usecase_output import CreateCommentUsecaseOutput


class CreateCommentUsecaseInteractor(object):
    __input: CreateCommentUsecaseInput
    __repository: CommentRepository

    def __init__(self, input: CreateCommentUsecaseInput) -> None:
        self.__input = input
        self.__repository = CommentRepository()

    def handle(self) -> CreateCommentUsecaseOutput:
        new_comment = NewComment(
            user_id=self.__input.user_id.value,
            spot_id=self.__input.spot_id.value,
            comment=self.__input.comment.value
        )
        comment = self.__repository.create(new_comment)
        return CreateCommentUsecaseOutput(is_success=True, comment=comment)

from app.core.sqlalchemy.data_model.comment_data_model import CommentDataModel
from app.usecase.comment.create.create_comment_usecase_output import (
    CreateCommentUsecaseOutput)


class CommentsCreateViewModel(object):
    __output: CreateCommentUsecaseOutput

    def __init__(self, output: CreateCommentUsecaseOutput) -> None:
        self.__output = output

    def convertToFastApi(self) -> CreateCommentUsecaseOutput:
        return {
            'is_success': self.__output.is_success,
            'error': self.__output.error,
            'comment': self.__create_comment_data_model()
        }

    def __create_comment_data_model(self):
        if self.__output.comment is None:
            return None
        return CommentDataModel(
            id=self.__output.comment.id.value,
            user_id=self.__output.comment.user_id.value,
            spot_id=self.__output.comment.spot_id.value,
            comment=self.__output.comment.comment.value,
            created_at=self.__output.comment.created_at.value,
            updated_at=self.__output.comment.updated_at.value
        )

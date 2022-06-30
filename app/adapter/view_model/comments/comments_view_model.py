from typing import List
from app.core.sqlalchemy.data_model.comment_data_model import (
    CommentWithUserDataModel)
from app.usecase.comment.fetch_comments.fetch_comments_usecase_output import (
    FetchCommentsUsecaseOutput)
from app.domain.entity.comment import CommentWithUser
from app.domain.entity.user import User


class CommentsViewModel(object):
    __output: FetchCommentsUsecaseOutput

    def __init__(self, output: FetchCommentsUsecaseOutput) -> None:
        self.__output = output

    def convertToFastApi(self):
        return {
            'is_success': self.__output.is_success,
            'error': self.__output.error,
            'comments': self.__create_comments_list()
        }

    def __create_comments_list(self) -> List[CommentWithUserDataModel]:
        if self.__output.comments is None:
            return None
        return list(map(self.__create_comment_data_model,
                        self.__output.comments))

    def __create_comment_data_model(self, comment: CommentWithUser):
        return CommentWithUserDataModel(
            id=comment.id.value,
            user_id=comment.user_id.value,
            spot_id=comment.spot_id.value,
            comment=comment.comment.value,
            user=self.__create_user_data_model(comment.user)
        )

    def __create_user_data_model(self, user: User):
        return User(
            id=user.id.value,
            name=user.name.value,
            email=user.email.value,
            password=user.password.value
        )

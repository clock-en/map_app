from typing import List, Union
from app.core.sqlalchemy.data_model.comment_data_model import (
    CommentWithUserDataModel)
from app.core.sqlalchemy.data_model.user_data_model import UserDataModel
from app.domain.entity.comment import CommentWithUser
from app.domain.entity.user import User
from app.domain.value_object.id import Id
from app.domain.value_object.email import Email
from app.domain.value_object.password import Password
from app.domain.value_object.comment.comment_content import CommentContent
from app.domain.value_object.user.user_name import UserName
from app.infrastructure.dao.comment_dao import CommentDao


class CommentQueryService(object):
    __comment_dao: CommentDao

    def __init__(self) -> None:
        self.__comment_dao = CommentDao()

    def fetch_comments_by_spot_id(
        self,
        spot_id: int
    ) -> Union[List[CommentWithUser], None]:
        db_comment = self.__comment_dao.get_comments_by_spot_id(spot_id)
        if db_comment is None:
            return None
        return list(map(self.__create_comment_with_user_entity, db_comment))

    def __create_comment_with_user_entity(
        self,
        db_comment: CommentWithUserDataModel
    ) -> CommentWithUser:
        return CommentWithUser(
            id=Id(db_comment.id),
            user_id=Id(db_comment.user_id),
            spot_id=Id(db_comment.spot_id),
            comment=CommentContent(db_comment.comment),
            user=self.__create_user_entity(db_comment.user)
        )

    def __create_user_entity(self, db_user: UserDataModel) -> User:
        return User(
            id=Id(db_user.id),
            name=UserName(db_user.name),
            email=Email(db_user.email),
            password=Password(db_user.password)
        )

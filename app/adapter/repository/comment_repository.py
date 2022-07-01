from app.core.sqlalchemy.data_model.user_data_model import UserDataModel
from app.domain.entity.comment import Comment
from app.domain.entity.user import User
from app.domain.value_object.id import Id
from app.domain.value_object.email import Email
from app.domain.value_object.password import Password
from app.domain.value_object.ja_datetime import JaDatetime
from app.domain.value_object.comment.comment_content import CommentContent
from app.domain.value_object.user.user_name import UserName
from app.domain.value_object.comment.new_comment import NewComment
from app.infrastructure.dao.comment_dao import CommentDao


class CommentRepository(object):
    __comment_dao: CommentDao

    def __init__(self) -> None:
        self.__comment_dao = CommentDao()

    def create(self, new_comment: NewComment) -> Comment:
        db_comment = self.__comment_dao.create_comment(new_comment)
        return Comment(
            id=Id(db_comment.id),
            user_id=Id(db_comment.user_id),
            spot_id=Id(db_comment.spot_id),
            comment=CommentContent(db_comment.comment),
            user=self.__create_user_entity(db_comment.user),
            created_at=JaDatetime(db_comment.created_at),
            updated_at=JaDatetime(db_comment.updated_at)
        )

    def __create_user_entity(self, db_user: UserDataModel) -> User:
        return User(
            id=Id(db_user.id),
            name=UserName(db_user.name),
            email=Email(db_user.email),
            password=Password(db_user.password),
            created_at=JaDatetime(db_user.created_at),
            updated_at=JaDatetime(db_user.updated_at)
        )

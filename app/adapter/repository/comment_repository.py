from app.infrastructure.dao.comment_dao import CommentDao
from app.domain.entity.comment import Comment
from app.domain.value_object.id import Id
from app.domain.value_object.ja_datetime import JaDatetime
from app.domain.value_object.comment.comment_content import CommentContent
from app.domain.value_object.comment.new_comment import NewComment


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
            created_at=JaDatetime(db_comment.created_at),
            updated_at=JaDatetime(db_comment.updated_at)
        )

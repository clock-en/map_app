from app.core.sqlalchemy.data_model.comment_data_model import (
    CommentDataModel, CommentWithUserDataModel)
from app.core.sqlalchemy.data_model.user_data_model import UserDataModel
from app.domain.value_object.id import Id
from app.domain.value_object.comment.new_comment import NewComment
from .dao import Dao


class CommentDao(Dao):
    def get_comments_by_spot_id(self, spot_id: Id):
        return self.db.query(CommentWithUserDataModel).filter(
            CommentWithUserDataModel.spot_id == spot_id.value
        ).outerjoin(
            UserDataModel,
            UserDataModel.id == CommentWithUserDataModel.user_id
        ).all()

    def create_comment(self, comment: NewComment):
        new_comment = CommentDataModel(
            user_id=comment.user_id.value,
            spot_id=comment.spot_id.value,
            comment=comment.comment.value
        )
        self.db.add(new_comment)
        self.db.commit()
        self.db.refresh(new_comment)
        return new_comment

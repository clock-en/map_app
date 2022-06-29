from app.core.sqlalchemy.data_model.comment_data_model import CommentDataModel
from app.domain.value_object.comment.new_comment import NewComment
from .dao import Dao


class CommentDao(Dao):
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

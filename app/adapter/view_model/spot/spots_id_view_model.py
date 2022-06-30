from typing import Union
from app.core.sqlalchemy.data_model.spot_data_model import (
    SpotWithCommentsDataModel)
from app.core.sqlalchemy.data_model.comment_data_model import CommentDataModel
from app.domain.entity.comment import Comment
from app.usecase.spot.fetch_spot.fetch_spot_usecase_output import (
    FetchSpotUsecaseOutput)


class SpotsIdViewModel(object):
    __output: FetchSpotUsecaseOutput

    def __init__(self, output: FetchSpotUsecaseOutput) -> None:
        self.__output = output

    def convertToFastApi(self) -> FetchSpotUsecaseOutput:
        return {
            'is_success': self.__output.is_success,
            'error': self.__output.error,
            'spot': self.__create_spot_with_comments_data_model()
        }

    def __create_spot_with_comments_data_model(
        self
    ) -> Union[SpotWithCommentsDataModel, None]:
        if self.__output.spot is None:
            return None

        comments = []
        if self.__output.spot.comments:
            comments = list(map(self.__create_comment_data_model,
                                self.__output.spot.comments))

        return SpotWithCommentsDataModel(
            id=self.__output.spot.id.value,
            name=self.__output.spot.name.value,
            description=self.__output.spot.description.value,
            latitude=self.__output.spot.latitude.value,
            longitude=self.__output.spot.longitude.value,
            user_id=self.__output.spot.user_id.value,
            comments=comments
        )

    def __create_comment_data_model(
        self,
        comment: Comment
    ) -> CommentDataModel:
        return CommentDataModel(
            id=comment.id.value,
            user_id=comment.user_id.value,
            spot_id=comment.spot_id,
            comment=comment.comment.value
        )

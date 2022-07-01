from app.adapter.view_model.comments.comments_create_view_model import (
    CommentsCreateViewModel)
from app.usecase.comment.create.create_comment_usecase_output import (
    CreateCommentUsecaseOutput)


class CommentsCreatePresenter(object):
    __output: CreateCommentUsecaseOutput

    def __init__(self, output: CreateCommentUsecaseOutput) -> None:
        self.__output = output

    def api(self):
        viewModel = CommentsCreateViewModel(self.__output)
        return viewModel.convertToFastApi()

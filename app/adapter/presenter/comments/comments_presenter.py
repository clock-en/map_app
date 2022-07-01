from app.adapter.view_model.comments.comments_view_model import (
    CommentsViewModel)
from app.usecase.comment import (
    FetchCommentsUsecaseOutput)


class CommentsPresenter(object):
    __output: FetchCommentsUsecaseOutput

    def __init__(self, output: FetchCommentsUsecaseOutput) -> None:
        self.__output = output

    def api(self):
        viewModel = CommentsViewModel(self.__output)
        return viewModel.convertToFastApi()

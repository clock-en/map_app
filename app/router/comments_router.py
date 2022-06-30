from typing import List
from fastapi import APIRouter, Body, Depends, HTTPException, status
from app.core.sqlalchemy.schema import comments_schema
from app.core.sqlalchemy.schema import users_schema
from app.adapter.presenter.comments import (
    CommentsPresenter, CommentsCreatePresenter)
from app.usecase.comment import (
    FetchCommentsUsecaseInput,
    FetchCommentsUsecaseInteractor,
    CreateCommentUsecaseInput,
    CreateCommentUsecaseInteractor,
)
from app.domain.value_object.error.unprocessable_entity_error import (
    UnprocessableEntityError)
from app.utility import auth

router = APIRouter(prefix='/api/comments', tags=['comments'])


@router.get(
    '',
    response_model=List[comments_schema.CommentWithUser],
    status_code=status.HTTP_201_CREATED,
    dependencies=[Depends(auth.authorize_user)]
)
async def get_comments(
    spot_id: int,
):
    input = FetchCommentsUsecaseInput(spot_id)
    usecase = FetchCommentsUsecaseInteractor(input)
    presenter = CommentsPresenter(usecase.handle())
    viewModel = presenter.api()
    return viewModel['comments']


@router.post(
    '',
    response_model=comments_schema.Comment,
    status_code=status.HTTP_201_CREATED,
    dependencies=[Depends(auth.validate_content_type)]
)
async def create_comment(
    comment: comments_schema.CommentCreate = Body(embed=False),
    current_user: users_schema.User = Depends(auth.authorize_with_x_token)
):
    input = CreateCommentUsecaseInput(
        user_id=current_user.id,
        spot_id=comment.spot_id,
        comment=comment.comment,
    )
    usecase = CreateCommentUsecaseInteractor(input)
    presenter = CommentsCreatePresenter(usecase.handle())
    viewModel = presenter.api()

    if not viewModel['is_success']:
        if viewModel['error'].type == UnprocessableEntityError.TYPE_CODE:
            raise HTTPException(
                status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
                detail=[{
                    'loc': ['body', viewModel['error'].field],
                    'msg': viewModel['error'].message,
                    'type': 'value_error.' + viewModel['error'].field
                }])
    return viewModel['comment']

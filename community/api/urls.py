from django.urls import path
from community.api.views import (getRoutes,
                    GroupSearchView, GroupCreateView, GroupDestroyView, GroupJoinView, GroupLeaveView,
                    PostLikeView, PostCommentView, PostCreateView, PostUpdateView,
                    PostDestroyView, CommentDeleteView)

urlpatterns = [
    path('group/', GroupCreateView.as_view(), name='group-create'),
    path('group/search/', GroupSearchView.as_view(), name='group-search'),
    path('group/<uuid:id>/', GroupDestroyView.as_view(), name='group-delete'),
    path('group/<uuid:id>/join/', GroupJoinView.as_view(), name='group-join'),
    path('group/<uuid:id>/leave/', GroupLeaveView.as_view(), name='group-leave'),
    path('post/create/', PostCreateView.as_view(), name='post-create'),
    path('post/<uuid:id>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<uuid:id>/delete/', PostDestroyView.as_view(), name='post-delete'),
    path('post/<uuid:id>/like/', PostLikeView.as_view(), name='post-like'),
    path('post/<uuid:id>/comment/', PostCommentView.as_view(), name='post-comment'),
    path('post/comments/<str:id>/', CommentDeleteView.as_view(), name='comment-delete'),
]
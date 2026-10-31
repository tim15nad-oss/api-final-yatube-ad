from django.urls import path, include
from rest_framework.routers import DefaultRouter
from api.views import (
    PostViewSet, CommentViewSet, FollowViewSet, GroupViewSet
)

router = DefaultRouter()
router.register(r'posts', PostViewSet, basename='posts')
router.register(r'follow', FollowViewSet, basename='follow')
router.register(r'groups', GroupViewSet, basename='groups')

comment_list = CommentViewSet.as_view({
    'get': 'list', 'post': 'create'
})
comment_detail = CommentViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})

urlpatterns = [
    path('posts/<int:post_id>/comments/', comment_list, name='comments-list'),
    path(
        'posts/<int:post_id>/comments/<int:pk>/',
        comment_detail,
        name='comments-detail'
    ),
    path('', include(router.urls)),
]

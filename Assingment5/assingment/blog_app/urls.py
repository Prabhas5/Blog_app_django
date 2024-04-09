from django.urls import path
from .views import PostListCreateAPIView,CommentListCreateAPIView,PostDetailUpdateDeleteAPIView,PostListAPIView

urlpatterns=[
    path("list_create/",PostListCreateAPIView.as_view(),name="create_view"),
    path("detail/<int:pk>/",PostDetailUpdateDeleteAPIView.as_view(),name="detail_put_update_delete"),
    path("comment/<int:post_id>/",CommentListCreateAPIView.as_view(),name="add_comment"),
    path('',PostListAPIView.as_view(),name="view_all_post")
    

]
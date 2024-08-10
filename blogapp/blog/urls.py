from django.urls import path, include
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView, LikeView, CommentCreateView
from . import views

urlpatterns = [

    path("", PostListView.as_view(), name="blog-home"),
    path("post/<int:pk>/", PostDetailView.as_view(), name="post-detail"),
    path("post/new/", PostCreateView.as_view(), name="post-create"),
    path("post/<int:pk>/update", PostUpdateView.as_view(), name="post-update"),
    path("like/<int:pk>/", LikeView, name="like-post"),
    path("post/<int:pk>/comment/", CommentCreateView.as_view(), name="comment-create"),
    path("post/<int:pk>/delete", PostDeleteView.as_view(), name="post-delete"),
    path("about/", views.about, name="blog-about"),
]

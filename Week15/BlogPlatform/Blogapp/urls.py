from django.urls import path
from .views import home, view_post, post_detail, view_author, author_detail

urlpatterns = [
    path("home/", home),
    path("posts/", view_post),
    path("posts/<int:pk>/", post_detail, name="post_detail"),
    path("authors/", view_author),
    path("authors/<int:pk>/", author_detail, name="author_detail"),
]

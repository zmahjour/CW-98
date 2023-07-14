from django.urls import path
from . import views

urlpatterns = [
    path("home/", views.home),
    path("posts/", views.view_post),
    path("posts/<int:pk>/", views.post_detail, name="post_detail"),
    path("authors/", views.view_author),
]

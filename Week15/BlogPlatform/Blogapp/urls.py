from django.urls import path
from . import views

urlpatterns = [
    path("home/", views.home),
    path("posts/", views.view_post),
    path("authors", views.view_author),
]

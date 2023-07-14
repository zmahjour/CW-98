from django.urls import path
from .views import view_category, category_detail

urlpatterns = [
    path("categories/", view_category),
    path("categories/<int:pk>/", category_detail, name="category_detail"),
]

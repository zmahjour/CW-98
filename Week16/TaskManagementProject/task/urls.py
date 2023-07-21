from django.urls import path
from task import views

urlpatterns = [
    path("home/", views.home, name="home"),
    path("search/", views.search, name="search"),
    path("detail/<int:task_id>/", views.task_detail, name="task_detail"),
    path("all/", views.all_tasks, name="all_tasks"),
    path("categories/", views.categories, name="categories"),
    path(
        "addfromcategory/<int:category_id>/",
        views.add_from_category,
        name="add_from_category",
    ),
]

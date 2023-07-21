from django.urls import path
from task import views

urlpatterns = [
    path("home/", views.home, name="home"),
    path("search/", views.search, name="search"),
    path("detail/<int:task_id>/", views.task_detail, name="task_detail"),
    path("all/", views.all_tasks, name="all_tasks"),
    path("categories/", views.categories, name="categories"),
    path(
        "category_detail/<int:category_id>/",
        views.category_detail,
        name="category_detail",
    ),
    # path("update/<int:category_id>/", views.update_category, name="update_category"),
]

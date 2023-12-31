from django.urls import path
from task import views

urlpatterns = [
    path("home/", views.home, name="home"),
    path("search/", views.search, name="search"),
    path("detail/<int:pk>/", views.TaskDetailView.as_view(), name="task_detail"),
    path("all/", views.AllTasksView.as_view(), name="all_tasks"),
    path("categories/", views.AllCategoriesView.as_view(), name="categories"),
    path(
        "category_detail/<int:category_id>/",
        views.category_detail,
        name="category_detail",
    ),
    path(
        "update_category/<int:category_id>/",
        views.update_category,
        name="update_category",
    ),
    path(
        "delete_category/<int:category_id>/",
        views.delete_category,
        name="delete_category",
    ),
    path("delete_task/<int:task_id>/", views.delete_task, name="delete_task"),
    path("task_create/", views.TaskCreateView.as_view(), name="task_create"),
]

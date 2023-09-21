from django.urls import path
from .views import TaskListView, TaskDetailView, UserListView, UserDetailView, taskView, taskCreate


# Define the urlpattern

urlpatterns = [
    path("api/task", TaskListView.as_view(), name="api-task-list-view"),
    path("api/task/<int:pk>", TaskDetailView.as_view(), name='api-single-task-view'),
    path("api/user", UserListView.as_view(), name="api-user-list-view"),
    path("api/user/<int:pk>", UserDetailView.as_view(), name='api-user-task-view'),

    path("task/", taskView, name="task-view"), 
    path("task-create/", taskCreate, name="task_create"),
]
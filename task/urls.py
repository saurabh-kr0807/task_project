from django.urls import path, include, re_path
from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('task/', views.TaskListView.as_view(), name='task_list'),
    re_path(r'^task/(?P<pk>\d+)/', views.TaskDetailView.as_view(), name='task_detail'),
    path('task/new/', views.CreateTaskView.as_view(), name='task_new'),
    path('task/P<pk>/edit/', views.TaskUpdateView.as_view(), name='task_edit'),
    path('task/P<pk>/delete/', views.TaskDeleteView.as_view(), name='task_remove'),
]

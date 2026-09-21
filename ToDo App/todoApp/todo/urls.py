from django.urls import path
from . import views

app_name = 'todo'

urlpatterns = [
    path('', views.task_list, name = 'task_list'),
    path('add/', views.add_task, name = 'add_task'),
    path('edit/<int:taskID>/', views.edit_task, name = 'edit_task'),
    path('delete/<int:taskID>/', views.delete_task, name = 'delete_task'),
    path('toggle/<int:taskID>/', views.toggle_task, name = 'toggle_task'),
]

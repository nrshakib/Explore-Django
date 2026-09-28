from django.urls import path
from . import views

urlpatterns = [
    path('users/', views.get_users, name = 'get_users'),
    path('users/add-user/',views.add_users, name = 'add_users'),
    path('users/update-user/<int:id>',views.update_user, name = 'update_user'),
    path('users/delete-user/<int:id>',views.delete_user, name = 'delete_user'),

]

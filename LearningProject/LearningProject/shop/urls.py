from django.urls import path
from . import views

urlpatterns = [
    path('', views.home , name = 'Shop Home'),
    path('products/', views.products, name = 'Shop Products')
]
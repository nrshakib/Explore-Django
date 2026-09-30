from django.urls import path
from .views import CustomerListCreateAPI, CustomerRetrieveUpdateDestroy

urlpatterns = [
    path('customer/', CustomerListCreateAPI.as_view()),
    path('customer/<int:pk>/', CustomerRetrieveUpdateDestroy.as_view()),
]

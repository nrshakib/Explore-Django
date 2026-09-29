from django.urls import path
from .views import TeachersApi

urlpatterns = [
    path('teachers/', TeachersApi.as_view()),
    path('teachers/<int:id>/', TeachersApi.as_view()),
]

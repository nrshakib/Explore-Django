from django.urls import path
from . import views

urlpatterns = [
    path('', views.article_details, name = 'Article Details')
]

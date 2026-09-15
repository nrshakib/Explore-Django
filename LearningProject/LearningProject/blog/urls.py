from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.home, name = 'Blog Home'),
    path('about/', views.about, name = 'Blog About'),

    # url parameters

    # path
    path('<int:blog_id>/', views.blog_details, name = 'Blog Details'),
    path('user/<str:user_name>/', views.user_profile, name = 'User Profile'),

    # multiple params
    path('year/<int:year>/<int:month>', views.blog_by_year_month, name = 'Blog By Year Month'),

    # regex_path
    re_path(r'^year/(?P<year>[0-9]{4})/$',
            views.blog_by_year,
            name='Blog by year')

    
]
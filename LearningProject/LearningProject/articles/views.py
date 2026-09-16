from django.shortcuts import render
from datetime import datetime

def article_details(request):
    post = {
        'title':"Article Title",
        'desc':'This is django',
        'author': None,
        'date': datetime(2026, 9, 16, 2,50),
        'comments': 5,
        'tags':['Django', 'Python', 'Backend'],
        'price': 100,
        'number': 7
    }
    return render(request, 'article/blog_details.html',{
        "post": post
    } )
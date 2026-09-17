from django.shortcuts import render
from datetime import datetime

def books(request):
    books = [
        {'title':'Django', 'is_featured':True, 'author':'John'},
        {'title':'Python', 'is_featured':False, 'author':'Doe'},
        {'title':'React', 'is_featured':True, 'author':''}
    ]
    context = {
        "books": books,
        'today': datetime.now(),
        'html':'<h1>Hello World</h1>'
    }
    return render(request, 'books/book_list.html',context)

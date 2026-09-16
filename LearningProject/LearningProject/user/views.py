from django.shortcuts import render
from datetime import datetime

class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def home(request):
        context = {
            "name": 'John Doe',
            'age': 25,
            'skill': ["Js", 'Python'],
            'user': User('JD', 28),
        }

        return render(request, 'home.html', context)
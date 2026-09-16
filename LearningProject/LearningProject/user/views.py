from django.shortcuts import render

class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age

def home(request):
        context = {
            "name": 'John Doe',
            'age': 25,
            'skills': ["Js", 'Python'],
            'user': User('JD', 28),
        }

        return render(request, 'user/home.html', context)
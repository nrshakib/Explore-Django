from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def Home(request):
    return HttpResponse("Welcome to home page")

def about(request):
    return HttpResponse("Welcome to about page")
from django.http import HttpResponse

def home(request):
    return HttpResponse('Welcome to Blog Home')

def about(request):
    return HttpResponse('Welcome to Blog About')
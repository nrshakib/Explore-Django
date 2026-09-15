from django.http import HttpResponse

def home(request):
    return HttpResponse('Welcome to shop home')

def products(request):
    return HttpResponse('Welcome to shop products')


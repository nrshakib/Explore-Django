from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Contact

def contact(request):
    return render(request, 'contact.html')

def submit(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        if name and email and message:
            Contact.objects.create(name = name,email = email, message = message)
            return HttpResponse(f'Thank you {name} for your message')
        else:
            return HttpResponse('Please type name, email and message')

    return redirect('contact.html')
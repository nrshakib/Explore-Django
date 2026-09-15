from django.http import HttpResponse

def home(request):
    return HttpResponse('Welcome to Blog Home')

def about(request):
    return HttpResponse('Welcome to Blog About')

def blog_details(request, blog_id):
    return HttpResponse(f'Blog details {blog_id}')

def user_profile(request, user_name):
    return HttpResponse(f'User name: {user_name}')

def blog_by_year(request, year):
    return HttpResponse(f'Blog of {year}')

def blog_by_year_month(request, **kwargs):
    return HttpResponse(f'This blog is of Month: {kwargs['month']}, Year: {kwargs['year']}')
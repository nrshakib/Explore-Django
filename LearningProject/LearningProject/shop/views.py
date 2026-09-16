from django.shortcuts import render

def items_list(request):
    return render(request, 'shop/item_list.html')
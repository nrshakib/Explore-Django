from django.contrib import admin
from .models import Customers

# Register your models here.
@admin.register(Customers)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'address', 'phone')
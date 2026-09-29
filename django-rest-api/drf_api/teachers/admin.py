from django.contrib import admin
from .models import Teachers

# Register your models here.
@admin.register(Teachers)
class AdminTeacher(admin.ModelAdmin):
    list_display = ('id', 'name', 'department')
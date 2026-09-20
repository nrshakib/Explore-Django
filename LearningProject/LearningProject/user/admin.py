from django.contrib import admin
from user.models import User

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display= ('name', 'age', 'city')
    search_fields = ('name', 'city')
    list_filter = ('name', 'age', 'city')
    ordering = ('name',)



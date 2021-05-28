# Django
from django.contrib import admin

# Models
from users.models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):

    list_display = ('pk', 'username', 'email')
    list_display_links = ('pk', 'username',)
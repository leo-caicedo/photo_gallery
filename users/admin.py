# Django
from django.contrib import admin
from django.contrib.admin.decorators import register
from django.shortcuts import redirect

# Models
from users.models import User

admin.site,register(User)
# Django
from django.urls import path

# Views
from users.views import main

app_name = 'users'
urlpatterns = [
    path('users', main)
]
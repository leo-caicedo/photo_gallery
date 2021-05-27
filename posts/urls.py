# Django
from django.urls import path

# Views
from posts.views import main

app_name = 'posts'
urlpatterns = [
    path('', main)
]
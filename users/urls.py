# Django
from django.contrib.auth.views import LoginView
from django.urls import path

# Views
from users.views import main, Login
from django.contrib.auth.views import LogoutView

app_name = 'users'
urlpatterns = [
    path('', main),
    path('login', Login.as_view(), name='login'),
    path('logout', LogoutView.as_view(), name='logout'),
]
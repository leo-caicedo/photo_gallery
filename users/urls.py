# Django
from django.urls import path

# Views
from users.views import Login, SignUp
from django.contrib.auth.views import LogoutView

app_name = 'users'
urlpatterns = [
    path('login', Login.as_view(), name='login'),
    path('logout', LogoutView.as_view(), name='logout'),
    path('signup', SignUp.as_view(), name='signup'),
]

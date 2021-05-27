# Django
from django.shortcuts import render
from django.contrib.auth.views import LoginView

def main(request):
    return render(request, 'users/base.html')


class Login(LoginView):

    template_name = 'users/login.html'
    fields = '__all__'
    redirect_authenticated_user = True
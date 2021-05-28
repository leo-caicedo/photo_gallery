# Django
from django.contrib.auth import login
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView
from django.views.generic import FormView

# Forms
from users.forms import UserCreationForm


class Login(LoginView):

    template_name = 'users/login.html'
    fields = '__all__'
    redirect_authenticated_user = True


class SignUp(FormView):

    template_name = 'users/signup.html'
    form_class = UserCreationForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('posts:feed')

    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super(SignUp, self).form_valid(form)
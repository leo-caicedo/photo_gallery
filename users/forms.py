# Django
from django.contrib.auth.forms import UserCreationForm
from django.db import models

# Models
from users.models import User


class UserCreationForm(UserCreationForm):

    class Meta:
        model = User
        fields = ('username','email')
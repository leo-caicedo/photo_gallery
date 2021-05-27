# Django
from django.db import models
from django.contrib.auth.models import AbstractUser

# Utilities
from utils.models import DateModel


class User(DateModel, AbstractUser):
    """User model.

    Customize the user model, Change the username field to email. 
    """

    email = models.EmailField(
        unique=True,
        error_messages={
            'unique': 'A user with that email already exists.'
        }
    )

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        """Return username."""
        return self.username

    def get_short_name(self):
        """Return username."""
        return self.username
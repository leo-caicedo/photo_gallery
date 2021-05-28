# Django
from django.db import models

# Models
from users.models import User
from utils.models import DateModel


class Post(DateModel, models.Model):
    """Post model.

    This model provided the atributes
    of the photos saved by the user
    """

    user = models.ForeignKey(User, on_delete=models.CASCADE)

    title = models.CharField(max_length=30)
    photo = models.ImageField(upload_to='posts/photos')

    def __str__(self):
        return self.title
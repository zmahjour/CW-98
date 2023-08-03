from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class User(AbstractUser):
    photo = models.ImageField(upload_to="user_photos/", blank=True, null=True)

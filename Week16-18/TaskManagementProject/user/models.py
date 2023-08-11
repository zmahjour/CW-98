from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from .managers import CustomUserManager


class CustomUser(AbstractBaseUser):
    username = models.CharField(max_length=50, unique=True)
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=50, blank=True, null=True)
    last_name = models.CharField(max_length=50, blank=True, null=True)
    photo = models.ImageField(upload_to="user_images/", blank=True, null=True)
    is_admin = models.BooleanField(default=False)

    objects = CustomUserManager()


    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username", "first_name", "last_name"]


    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin
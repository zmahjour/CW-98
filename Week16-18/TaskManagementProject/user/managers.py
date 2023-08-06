from typing import Any
from django.contrib.auth.models import BaseUserManager


class CustomUserManager(BaseUserManager):
    def create_user(self, username, email, first_name, last_name, photo, password):
        if not username:
            raise ValueError("User must have username")
        if not email:
            raise ValueError("User must have email")

        user = self.model(
            username=username,
            email=self.normalize_email(email),
            first_name=first_name,
            last_name=last_name,
            photo=photo,
        )
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, username, email, first_name, last_name, photo, password):
        user = self.create_user(username, email, first_name, last_name, photo, password)
        user.is_admin = True
        user.save(using=self._db)
        return user

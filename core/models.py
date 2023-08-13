from django.db import models

# Create your models here.

from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin
)


class UserManager(BaseUserManager):
    """ **extra_field means user can provide keyword arguments """
    def create_user(self, email, password=None, **extra_field):
        user = self.model(email=email, **extra_field)
        user.set_password(password)
        user.save(using=self._db)
        return user


""" PermissionsMixin is for Functionality for the permissions and fields """
""" AbstractBaseUser is for Functionality for the auth system """


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=25, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()
    USERNAME_FIELD = 'email'

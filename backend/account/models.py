from typing import Optional
from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager, PermissionsMixin, Permission, Group
# from django.contrib.auth.backends import BaseBackend

class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None):
        if not email:
            raise ValueError('Email is required')
        if not password:
            raise ValueError('Password is required')
        try:
            user = self.model(
                email = self.normalize_email(email),
            )
            user.set_password(password)
            user.save()

            return user
        except:
            raise ValueError('Please try again')

    def create_superuser(self, email, password=None, **extra_fields):
        try:
            user = self.create_user(
                email= email,
                password=password,
                is_admin=True,
                is_superuser=True,
                is_staff=True,
                **extra_fields
            )
            return user
        except:
            raise ValueError('An Error Occured Please Try Again')
        




class CustomUser(AbstractUser, PermissionsMixin):
    # name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_verified = models.BooleanField(default=False)
    groups = models.ManyToManyField(Group, related_name='user_groups', blank=True)
    user_permissions = models.ManyToManyField(Permission, related_name='user_permissions', blank=True)
    # username = None

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email

  
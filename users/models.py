"""
Users custom model.
"""

from django.db import models
from zoneinfo import available_timezones
from django.contrib.auth.models import AbstractUser, BaseUserManager


class CustomUserManager(BaseUserManager):
    """
    Custom user manager.
    """

    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("Error: Email is required!")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user
    
    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Super user must have is_staff=True")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Super user must have is_superuser=True")
        
        return self.create_user(email, password, **extra_fields)

class CustomUser(AbstractUser):
    """
    Custom user model attributes definition.
    """
    username = None
    email = models.EmailField(unique=True)

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    time_zone = models.CharField(max_length=50,
                                 choices=[(tz,tz) for tz in sorted(available_timezones())],
                                 default="Africa/Johannesburg", blank=False, null=False)


    USERNAME_FIELD = "email" #set email login
    REQUIRED_FIELDS = ["first_name", "last_name"]

    objects = CustomUserManager()

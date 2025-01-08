from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import BaseUserManager

from django.core.validators import RegexValidator
from django.db import models
from django.contrib.auth.models import AbstractUser


class UserManager(BaseUserManager):
    def create_user(self, phone_number, password, **extra_fields):
        if not phone_number:
            raise ValueError("User must have phone_number")
        user = self.model(phone_number=phone_number, **extra_fields)
        user.password = make_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, phone_number, password):
        if not password:
            raise ValueError("Superuser must have password")
        user = self.create_user(phone_number=phone_number, password=password)
        user.is_active = True
        user.is_superuser = True
        user.is_staff = True
        user.save()
        return user
    
    


class User(AbstractUser):
    username = models.CharField(max_length=155, unique=False, null=True, blank=True)
    phone_validator = RegexValidator(
        regex=r'^\+998\d{9}$',
        message="Yaroqsiz telefon raqam!"
    )
    phone_number = models.CharField(
        max_length=25,
        validators=[phone_validator],
        null=True,
        blank=True,
        unique=True
    )

    USERNAME_FIELD = 'phone_number'
    REQUIRED_FIELDS = []
    objects = UserManager()
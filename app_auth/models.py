from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from utilitas.models import BaseModel

from app_auth.managers import CustomUserManager

# enum thingy. Too lazy to use the enum lib


class UserType:
    teacher = "teacher"
    admin = "admin"
    student = "student"


class User(AbstractBaseUser, BaseModel, PermissionsMixin):
    """
    The user model
    """

    role_choices = [
        (UserType.teacher,) * 2,
        (UserType.admin,) * 2,
        (UserType.student,) * 2,
    ]

    email = models.EmailField(unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    role = models.CharField(max_length=128, choices=role_choices)

    groups = None
    user_permissions = None

    USERNAME_FIELD = "email"
    objects = CustomUserManager()

    def __str__(self):
        return f"<User: {self.id} {self.email}>"

    class Meta:
        ordering = ("id",)

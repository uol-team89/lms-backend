from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from utilitas.models import BaseModel

from app_auth.managers import CustomUserManager


class User(AbstractBaseUser, BaseModel, PermissionsMixin):
    """
    The user model
    """

    role_choices = [
        ("admin",) * 2,
        ("partnership-manager",) * 2,
        ("agent-leader",) * 2,
        ("agent-staff",) * 2,
        ("customer",) * 2,
    ]
    auth_method_choices = (("phone_number",) * 2, ("email",) * 2)

    email = models.EmailField(unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    groups = None
    user_permissions = None

    USERNAME_FIELD = "email"
    objects = CustomUserManager()

    def __str__(self):
        return f"<User: {self.id} {self.email}>"
    class Meta:
        ordering = ("id",)

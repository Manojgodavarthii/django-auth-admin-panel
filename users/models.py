from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager
)


class UserManager(BaseUserManager):

    def create_user(
        self,
        mobile,
        name,
        password=None,
        role='user'
    ):

        if not mobile:

            raise ValueError(
                "Mobile number is required"
            )

        user = self.model(
            mobile=mobile,
            name=name,
            role=role
        )

        user.set_password(password)
        user.save(
            using=self._db
        )

        return user

    def create_superuser(
        self,
        mobile,
        name,
        password=None
    ):

        user = self.create_user(
            mobile=mobile,
            name=name,
            password=password,
            role='admin'
        )

        user.is_staff = True
        user.is_superuser = True
        user.save(
            using=self._db
        )

        return user


class User(AbstractBaseUser):

    ROLE_CHOICES = (
        ('user', 'User'),
        ('admin', 'Admin'),
    )

    name = models.CharField(
        max_length=100
    )

    mobile = models.CharField(
        max_length=15,
        unique=True
    )

    role = models.CharField(
        max_length=10,
        choices=ROLE_CHOICES,
        default='user'
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    is_active = models.BooleanField(
        default=True
    )

    is_staff = models.BooleanField(
        default=False
    )

    is_superuser = models.BooleanField(
        default=False
    )

    objects = UserManager()

    USERNAME_FIELD = 'mobile'

    REQUIRED_FIELDS = ['name']

    def __str__(self):
        return self.mobile
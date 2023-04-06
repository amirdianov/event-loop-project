from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import (
    UserManager as DjangoUserManager,
    PermissionsMixin,
)
from django.db import models

from backend.web.enums import Role, CategoryEvent


# Create your models here.


class UserManager(DjangoUserManager):
    def _create_user(self, email, password, **extra_fields):
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.password = make_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password=None, **extra_fields):
        return self._create_user(email, password, role=Role.admin, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    object = UserManager()

    name = models.CharField(max_length=127)
    surname = models.CharField(max_length=127)
    role = models.CharField(choices=Role.choices, default=Role.user)
    email = models.EmailField(unique=True)

    EMAIL_FIELD = "email"
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    @property
    def is_staff(self):
        return self.role in (Role.stuff, Role.admin)

    @property
    def is_superuser(self):
        return self.role == Role.admin


class Tag(models.Model):
    title = models.CharField(max_length=127)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class Event(models.Model):
    title = models.CharField(max_length=127)
    description = models.TextField()
    start_time = models.DateTimeField()
    finish_time = models.DateTimeField()
    photo = models.ImageField()
    price = models.IntegerField()
    category = models.CharField(choices=CategoryEvent.choices)
    tag = models.ForeignKey(Tag, on_delete=models.SET_NULL, null=True, blank=True)
    is_passed = models.BooleanField()
    url = models.URLField(null=True, blank=True)


class UserEvent(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    is_organizer = models.BooleanField()


class Comment(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True, blank=True
    )  # if user unauthorized
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Rating(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True, blank=True
    )  # if user unauthorized
    count = models.IntegerField()


class BankOperation(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True, blank=True
    )  # if user unauthorized
    created_at = models.DateTimeField(auto_now_add=True)
    price = models.IntegerField()

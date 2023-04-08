from django.db import models


class Role(models.TextChoices):
    user = "user", "Пользователь"
    stuff = "stuff", "Сотрудник"
    admin = "admin", "Администратор"

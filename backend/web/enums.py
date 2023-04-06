from django.db import models


class CategoryEvent(models.TextChoices):
    lessons = "lessons", "Уроки"
    vebinars = "vebinars", "Вебинары"
    entertainments = "entertainments", "Развлечения"


class Role(models.TextChoices):
    user = "user", "Пользователь"
    stuff = "stuff", "Сотрудник"
    admin = "admin", "Администратор"

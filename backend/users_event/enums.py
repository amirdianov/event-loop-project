from django.db import models


class Category(models.TextChoices):
    lesson = "lesson", "Уроки"
    webinar = "webinar", "Вебинар"
    masterclass = "masterclass", "Мастер-класс"
    entertainments = "entertainments", "Развлечения"

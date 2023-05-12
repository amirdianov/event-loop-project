from django.db import models

from users_event.models import BaseManyToMany, Event, User


# Create your models here.
class Comment(BaseManyToMany):
    text = models.TextField()
    created_at = models.DateTimeField(auto_now=True)

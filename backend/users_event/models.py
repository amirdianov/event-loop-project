import os
from datetime import datetime

from django.db import models

from authorisation_token.models import User
from users_event.enums import Category


def get_note_image_path(instance, filename):
    return os.path.join("event_images", datetime.today().strftime("%Y-%m-%d"), filename)


class Tag(models.Model):
    title = models.CharField(max_length=200)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        unique_together = ("title", "user")

    def __str__(self):
        return self.title


class Event(models.Model):
    title = models.CharField(max_length=500)
    description = models.TextField()
    start_time = models.DateTimeField()
    finish_time = models.DateTimeField()
    photo = models.ImageField(
        upload_to=get_note_image_path, null=False, verbose_name="Картинка"
    )
    price = models.IntegerField(null=True, blank=True)
    category = models.CharField(choices=Category.choices)
    is_passed = models.BooleanField(default=False)
    url = models.URLField(null=True, blank=True)
    organizer = models.ManyToManyField(
        User, through="Participant", related_name="is_organizer"
    )
    rating_event = models.ManyToManyField(
        User, through="Rating", related_name="rating_event"
    )
    tags = models.ManyToManyField("Tag", blank=True)

    def __str__(self):
        return self.title


class BaseManyToMany(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    event = models.ForeignKey("Event", on_delete=models.CASCADE)

    class Meta:
        abstract = True


class Participant(BaseManyToMany):
    is_organizer = models.BooleanField()


class Rating(BaseManyToMany):
    rating = models.IntegerField()

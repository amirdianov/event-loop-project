import os

from django.db import models
from stdimage import StdImageField

from authorisation_token.models import User
from users_event.enums import Category

# TODO поля created_at, updated_at
def get_note_image_path(instance, filename):
    return os.path.join(
        "event_images", instance.start_time.strftime("%Y-%m-%d"), filename
    )


class Tag(models.Model):
    title = models.CharField(max_length=200)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class Event(models.Model):
    title = models.CharField(max_length=500)
    description = models.TextField()
    start_time = models.DateTimeField()
    finish_time = models.DateTimeField()
    photo = StdImageField(
        upload_to=get_note_image_path,
        null=False,
        verbose_name="Картинка",
        variations={
            "thumbnail": {
                "height": 400,
                "width": 400,
            }
        },
    )
    price = models.IntegerField(null=True, blank=True)
    category = models.CharField(choices=Category.choices)
    is_passed = models.BooleanField()
    url = models.URLField(null=True, blank=True)
    is_organizer = models.ManyToManyField(
        User, through="Participant", related_name="is_organizer"
    )
    rating_event = models.ManyToManyField(
        User, through="Rating", related_name="rating_event"
    )
    tags = models.ManyToManyField("Tag", blank=True)


class BaseManyToMany(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    event = models.ForeignKey("Event", on_delete=models.CASCADE)

    class Meta:
        abstract = True


class Participant(BaseManyToMany):
    is_organizer = models.BooleanField()


class Rating(BaseManyToMany):
    rating = models.IntegerField()

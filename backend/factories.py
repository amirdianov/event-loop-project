import random

import factory
from factory import SubFactory

from authorisation_token.models import User
from comments_system.models import Comment
from users_event.enums import Category
from users_event.models import Event, Participant, Tag


class UserFactory(factory.django.DjangoModelFactory):
    email = factory.Faker("email")

    class Meta:
        model = User


class EventFactory(factory.django.DjangoModelFactory):
    title = factory.Faker("sentence")
    start_time = factory.Faker("date_object")
    finish_time = factory.Faker("date_object")
    category = random.choice(Category.choices[0])

    class Meta:
        model = Event


class ParticipantFactory(factory.django.DjangoModelFactory):
    user = SubFactory(UserFactory)
    event = SubFactory(EventFactory)
    is_organizer = True

    class Meta:
        model = Participant


class CommentFactory(factory.django.DjangoModelFactory):
    user = SubFactory(UserFactory)
    event = SubFactory(EventFactory)
    text = factory.Faker("text")

    class Meta:
        model = Comment


class TagFactory(factory.django.DjangoModelFactory):
    user = SubFactory(UserFactory)
    title = factory.Faker("word")

    class Meta:
        model = Tag

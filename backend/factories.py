import factory
from factory import SubFactory

from authorisation_token.models import User
from comments_system.models import Comment
from users_event.models import Event, Participant, Tag


class UserFactory(factory.django.DjangoModelFactory):
    email = factory.Faker("email")

    class Meta:
        model = User


class EventFactory(factory.django.DjangoModelFactory):
    start_time = factory.Faker("date_object")
    finish_time = factory.Faker("date_object")

    class Meta:
        model = Event


class ParticipantFactory(factory.django.DjangoModelFactory):
    user = SubFactory(UserFactory)
    event = SubFactory(EventFactory)

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

    class Meta:
        model = Tag

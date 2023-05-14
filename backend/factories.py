import factory
from factory import SubFactory

from authorisation_token.models import User
from users_event.models import Event, Participant


class UserFactory(factory.django.DjangoModelFactory):
    email = factory.Faker("email")

    class Meta:
        model = User


class EventFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Event


class ParticipantFactory(factory.django.DjangoModelFactory):
    user = SubFactory(UserFactory)
    event = SubFactory(EventFactory)

    class Meta:
        model = Participant

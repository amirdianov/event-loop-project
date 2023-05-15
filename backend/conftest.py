import pytest
from rest_framework.test import APIClient
from rest_framework_simplejwt.tokens import RefreshToken

from factories import UserFactory, EventFactory, ParticipantFactory, CommentFactory


@pytest.fixture
def api_client():
    return APIClient()


@pytest.fixture(autouse=True)
def init_db(db):
    pass


@pytest.fixture
def jwt_token(user):
    refresh = RefreshToken.for_user(user)
    return {"Authorization": f"Bearer {str(refresh.access_token)}"}


@pytest.fixture
def user():
    return UserFactory()


@pytest.fixture
def event(user):
    return EventFactory()


@pytest.fixture
def participant(user, event):
    return ParticipantFactory(user=user, event=event)


# @pytest.fixture
# def comment(user, event):
#     return CommentFactory(user=user, event=event)

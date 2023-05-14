import pytest
from rest_framework.test import APIClient
from rest_framework_simplejwt.tokens import RefreshToken

from factories import UserFactory


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

import pytest
from rest_framework.test import APIClient

from factories import UserFactory


@pytest.fixture
def api_client():
    return APIClient()


@pytest.fixture(autouse=True)
def init_db(db):
    pass


@pytest.fixture
def user():
    return UserFactory()

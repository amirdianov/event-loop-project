# Create your tests here.
import pytest
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient


# Create your tests here.


@pytest.fixture
def api_client():
    return APIClient()


def test_status(api_client):
    response = api_client.get(reverse("status"))
    assert response.status_code == status.HTTP_200_OK


def test_registration(api_client):
    response = api_client.post(
        "/users/registration/",
        {"name": "Amir", "email": "b@gmail.com", "password": "12345"},
        format="json",
    )
    assert response.status_code == status.HTTP_201_CREATED

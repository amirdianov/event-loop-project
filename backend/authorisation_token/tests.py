# Create your tests here.
import pytest
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from rest_framework_simplejwt.tokens import RefreshToken


@pytest.fixture
def api_client():
    return APIClient()


@pytest.fixture(autouse=True)
def init_db(db):
    pass


# @pytest.fixture
# def user():
#     return User.objects.create_user(
#         name="TESTName",
#         surname="TESTSurname",
#         email="test@gmail.com",
#         password="TESTPassword",
#     )


@pytest.fixture
def jwt_token(user):
    refresh = RefreshToken.for_user(user)
    return {"Authorization": f"Bearer {str(refresh.access_token)}"}


def test_status(api_client):
    response = api_client.get(reverse("status"))
    assert response.status_code == status.HTTP_200_OK


def test_get_all_users(api_client, jwt_token):
    response = api_client.get(reverse("users-list"), headers=jwt_token)
    assert response.status_code == status.HTTP_200_OK


def test_registration(api_client):
    response = api_client.post(
        reverse("users-registration"),
        {
            "name": "TESTName",
            "surname": "TESTSurname",
            "email": "test@gmail.com",
            "password": "TESTPassword",
        },
        format="json",
    )
    assert response.status_code == status.HTTP_200_OK


def test_profile(api_client, jwt_token):
    response = api_client.get(reverse("users-profile"), headers=jwt_token)
    assert response.status_code == status.HTTP_200_OK


def test_forgot_password_view(api_client, user):
    response = api_client.post(reverse("forgot_password"), data={"email": user.email})
    assert response.status_code == status.HTTP_200_OK

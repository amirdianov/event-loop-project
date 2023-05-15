# Create your tests here.
import pytest
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.urls import reverse
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from rest_framework import status

from authorisation_token.enums import Role
from authorisation_token.models import User


@pytest.fixture
def user_data():
    return {
        "name": "John",
        "surname": "Doe",
        "email": "johndoe@example.com",
        "password": "p@ssw0rd",
    }


def test_create_user(user_data):
    user = User.objects.create_user(**user_data)
    assert user.email == user_data["email"]
    assert user.name == user_data["name"]
    assert user.surname == user_data["surname"]
    assert user.check_password(user_data["password"])


def test_create_superuser(user_data):
    superuser = User.objects.create_superuser(**user_data)
    assert superuser.is_staff == True
    assert superuser.is_superuser == True
    assert superuser.role == Role.admin


def test_is_staff(user):
    user.role = Role.user
    assert user.is_staff == False
    user.role = Role.stuff
    assert user.is_staff == True
    user.role = Role.admin
    assert user.is_staff == True


def test_is_superuser(user):
    user.role = Role.user
    assert user.is_superuser == False
    user.role = Role.stuff
    assert user.is_superuser == False
    user.role = Role.admin
    assert user.is_superuser == True


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


def test_user_update(api_client, user, jwt_token):
    response = api_client.patch(
        reverse("users-detail", args=(user.id,)),
        data={"name": "New", "surname": "NewNew"},
        headers=jwt_token,
    )
    assert response.status_code == status.HTTP_200_OK, response.content
    user.refresh_from_db()
    assert user.name == "New"


def test_forgot_password_view(api_client, user):
    response = api_client.post(reverse("forgot_password"), data={"email": user.email})
    assert response.status_code == status.HTTP_200_OK


def test_reset_password_view(api_client, user):
    token_generator = PasswordResetTokenGenerator()
    token = token_generator.make_token(user)
    uidb64 = urlsafe_base64_encode(force_bytes(user.pk))
    response = api_client.post(
        reverse("reset_password"),
        data={"password": "12345", "uid": uidb64, "token": token},
    )
    assert response.status_code == status.HTTP_200_OK
    response = api_client.post(
        reverse("reset_password"), data={"password": "12345", "uid": "", "token": token}
    )
    assert response.status_code == status.HTTP_400_BAD_REQUEST
    response = api_client.post(
        reverse("reset_password"),
        data={"password": "12345", "uid": uidb64, "token": ""},
    )
    assert response.status_code == status.HTTP_400_BAD_REQUEST

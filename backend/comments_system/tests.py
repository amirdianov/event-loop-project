# Create your tests here.
from django.urls import reverse
from rest_framework import status


def test_get_all_comments(api_client, jwt_token, participant):
    response = api_client.get(
        reverse("comments"),
        headers=jwt_token,
        data={"event_id": participant.event.id},
    )
    assert response.status_code == status.HTTP_200_OK


def test_comment_create(
    api_client,
    jwt_token,
    user,
    event,
):
    response = api_client.post(
        reverse("comments"),
        headers=jwt_token,
        data={"user": user.id, "event": event.id, "text": "Text"},
    )
    assert response.status_code == status.HTTP_201_CREATED

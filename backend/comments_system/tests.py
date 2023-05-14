# Create your tests here.
from django.urls import reverse
from rest_framework import status


def test_get_all_comments(api_client, jwt_token, participant):
    response = api_client.get(
        reverse("comments-list"),
        headers=jwt_token,
        params={"event_id": participant.event.id},
    )
    assert response.status_code == status.HTTP_200_OK

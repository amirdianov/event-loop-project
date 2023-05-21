# Create your tests here.
import os
from datetime import datetime

from django.urls import reverse
from rest_framework import status

from users_event.models import get_note_image_path


def test_event_str(event):
    assert event.title == event.__str__()


def test_tag_str(tag):
    assert tag.title == tag.__str__()


def test_get_note_image_path(tmp_path):
    instance = None
    filename = "test.jpg"
    expected_path = os.path.join(
        "event_images", datetime.today().strftime("%Y-%m-%d"), filename
    )

    path = get_note_image_path(instance, filename)

    assert path == expected_path


def test_get_user_subscriptions(api_client, jwt_token):
    response = api_client.get(reverse("subscriptions"), headers=jwt_token)
    assert response.status_code == status.HTTP_200_OK


def test_get_event_subscribers(api_client, event, jwt_token):
    response = api_client.get(
        reverse("subscribers"), headers=jwt_token, data={"event_id": event.id}
    )
    assert response.status_code == status.HTTP_200_OK


# TODO переписать - сделать вывод в ответ на post запрос - добавленный объект и у него проверять юзера
def test_user_subscribe(api_client, event, jwt_token, participant, user):
    print(event.start_time)
    response = api_client.post(
        reverse("subscribe"),
        headers=jwt_token,
        data={"event": {"id": event.id, "start_time": event.start_time}},
        format="json",
    )
    participant.refresh_from_db()
    assert participant.user == user


def test_get_users_tags(api_client, jwt_token, user, tag):
    response_create_tag = api_client.post(
        reverse("tags-list"), headers=jwt_token, data={"user": user.id, "title": "Test"}
    )
    assert response_create_tag.data["user"] == user.id
    response_get_tag = api_client.get(reverse("tags-list"), headers=jwt_token)
    assert len(response_get_tag.data) == 2
    assert "Test" == response_get_tag.data[1]["title"]


def test_create_rate(api_client, jwt_token, user, event):
    response = api_client.post(
        reverse("rate"),
        headers=jwt_token,
        data={"user": user.id, "event": event.id, "rating": 5},
    )
    assert response.status_code == status.HTTP_200_OK


def test_get_mean_rate(api_client, jwt_token, event):
    response = api_client.get(
        reverse("rate"), headers=jwt_token, data={"event_id": event.id}
    )
    assert response.status_code == status.HTTP_200_OK


def test_get_all_events(api_client, jwt_token):
    response = api_client.get(reverse("events-list"), headers=jwt_token)
    assert response.status_code == status.HTTP_200_OK


def test_get_all_events_with_slug(api_client, jwt_token, event):
    response = api_client.get(
        reverse("events-list"), headers=jwt_token, data={"slug": event.category}
    )
    assert len(response.data) == 1


def test_get_event(api_client, jwt_token, event):
    response = api_client.get(
        reverse("events-detail", args=(event.id,)), headers=jwt_token
    )
    assert response.status_code == status.HTTP_200_OK


def test_get_users_events(api_client, jwt_token, event, participant):
    response = api_client.get(reverse("my_events-list"), headers=jwt_token)
    assert response.status_code == status.HTTP_200_OK

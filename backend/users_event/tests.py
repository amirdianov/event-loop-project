# Create your tests here.
import os
from datetime import datetime

from users_event.models import get_note_image_path


def test_event_str(api_client, event):
    assert event.title == event.__str__()


def test_tag_str(api_client, tag):
    assert tag.title == tag.__str__()


def test_get_note_image_path(tmp_path):
    instance = None
    filename = "test.jpg"
    expected_path = os.path.join(
        "event_images", datetime.today().strftime("%Y-%m-%d"), filename
    )

    path = get_note_image_path(instance, filename)

    assert path == expected_path

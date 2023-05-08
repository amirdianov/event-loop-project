from django.conf import settings
from django.core.mail import send_mail
from django.db.models import Q
from django.utils import timezone

from eventloop.celery import app
from users_event.models import Event, Participant


# @app.task
# def test_task():
#     print("This is a test task!")


@app.task
def send_event_notification(event_id):
    event = Event.objects.get(id=event_id)
    subscribed_users = Participant.objects.filter(
        Q(event_id=event_id) & Q(is_organizer=False)
    )
    print("Я тут 3.0")

    print(subscribed_users, event, event_id)
    for subscription in subscribed_users:
        print("Я тут 4.0")
        msg_text = (
            f"Напоминаем вам о мероприятии {event.title}, которое начнется через час. "
        )
        if event.url:
            msg_text += f"Ссылка на мероприятие: {event.url}"
        send_mail(
            "Уведомление о мероприятии",
            f"Напоминаем вам о мероприятии {event.title}, которое начнется через час. Ссылка на мероприятие: {event.url}",
            settings.DEFAULT_FROM_EMAIL,
            [subscription.user.email],
            fail_silently=False,
        )


@app.task
def check_events():
    now = timezone.now()
    print("Я тут")
    print(now + timezone.timedelta(hours=1))
    events = Event.objects.filter(Q(start_time__lt=now + timezone.timedelta(hours=1)))
    print(events)
    for event in events:
        print("Я тут 2.0")
        send_event_notification.delay(event.id)

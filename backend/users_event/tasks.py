from django.conf import settings
from django.core.mail import send_mail
from django.db.models import Q
from django.utils import timezone

from eventloop.celery import app
from users_event.models import Event, Participant


@app.task
def send_event_notification(event_id):
    event = Event.objects.get(id=event_id)
    subscribed_users = Participant.objects.filter(
        Q(event_id=event_id) & Q(is_organizer=False)
    )

    for subscription in subscribed_users:
        if not subscription.sent_email:
            msg_text = f"Напоминаем вам о мероприятии {event.title}, которое начнется уже менее, чем через час! "
            if event.url is not None:
                msg_text += f"Ссылка на мероприятие: {event.url}"
            send_mail(
                "Уведомление о мероприятии",
                msg_text,
                settings.DEFAULT_FROM_EMAIL,
                [subscription.user.email],
                fail_silently=False,
            )
            subscription.sent_email = True
            subscription.save()

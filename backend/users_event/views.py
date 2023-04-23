from django.db.models import Prefetch
from rest_framework import viewsets

from users_event.models import Event, User
from users_event.serializers import EventInfoSerializer


# Create your views here.
class EventViewSet(viewsets.ModelViewSet):
    serializer_class = EventInfoSerializer

    def get_queryset(self):
        user_id = self.request.user.id
        qs = Event.objects.prefetch_related(
            Prefetch("organizer", User.objects.filter(id=user_id))
        )
        al = []
        for event in qs:
            org = [organizator for organizator in event.organizer.all()]
            al.append({"users": org})
        print(al)
        return Event.objects.prefetch_related(
            Prefetch("organizer", User.objects.filter(id=user_id))
        )

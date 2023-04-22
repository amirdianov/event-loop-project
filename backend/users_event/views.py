from rest_framework import viewsets

from users_event.models import Event
from users_event.serializers import EventInfoSerializer


# Create your views here.
class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventInfoSerializer

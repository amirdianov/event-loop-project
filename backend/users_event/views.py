from django.db.models import Prefetch
from rest_framework import mixins
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from users_event.models import Event, User
from users_event.serializers import EventInfoSerializer


# Create your views here.
class EventViewSet(
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    mixins.ListModelMixin,
    GenericViewSet,
):
    serializer_class = EventInfoSerializer

    def get_queryset(self, *args, **kwargs):
        if "user_id" in kwargs.keys():
            user_id = kwargs["user_id"]
            events = Event.objects.all()
            my_events_id = []
            for event in events:
                for obj in event.participant_set.all():
                    if user_id == obj.user_id and obj.is_organizer is True:
                        my_events_id.append(obj.event_id)
            return Event.objects.filter(id__in=my_events_id)
        else:
            return Event.objects.all()

    @action(detail=False, methods=["get"], permission_classes=[IsAuthenticated])
    def my_events(self, request, pk=None):
        queryset = self.filter_queryset(self.get_queryset(user_id=self.request.user.id))
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

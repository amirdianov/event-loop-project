from rest_framework import mixins
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet, ModelViewSet

from users_event.models import Event, Participant, Tag
from users_event.serializers import EventInfoSerializer, TagSerializer


class TagViewSet(mixins.ListModelMixin, GenericViewSet):
    pagination_class = None
    serializer_class = TagSerializer

    def get_queryset(self):
        return Tag.objects.filter(user=self.request.user)


class EventViewSet(
    mixins.RetrieveModelMixin,
    # mixins.UpdateModelMixin,
    # mixins.DestroyModelMixin,
    mixins.ListModelMixin,
    GenericViewSet,
):
    serializer_class = EventInfoSerializer

    def get_queryset(self, *args, **kwargs):
        if "slug" in self.request.GET.keys():
            category = self.request.GET["slug"]
            print(Event.objects.filter(category=category))
            return Event.objects.filter(category=category)
        else:
            return Event.objects.all()


class UserEventViewSet(
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    mixins.ListModelMixin,
    GenericViewSet,
):
    serializer_class = EventInfoSerializer

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset(user_id=self.request.user.id))
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

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

    def perform_create(self, serializer):
        obj = serializer.save()
        return obj

    def create_new_tag(self, request, title):
        print(request.user, title)
        new_tag = Tag(title=title, user=request.user)
        new_tag.save()
        return new_tag

    def create(self, request, *args, **kwargs):
        tag_names = request.data.getlist("tags")
        tags = []
        for tag_request in tag_names:
            try:
                tag = Tag.objects.get(id=tag_request)
            except (Tag.DoesNotExist, ValueError):
                tag = self.create_new_tag(request, tag_request)
            tags.append(tag.id)

        event_data = request.data.dict()
        event_data["tags"] = tags
        print(event_data)
        serializer = self.get_serializer(data=event_data)
        serializer.is_valid(raise_exception=True)
        event = self.perform_create(serializer)
        ans = Participant(user=request.user, event=event, is_organizer=True)
        ans.save()
        return Response(serializer.data)

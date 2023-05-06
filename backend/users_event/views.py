from django.conf import settings
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.core.mail import EmailMessage
from django.db.models import Avg, Q
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from rest_framework import mixins
from rest_framework.decorators import action, api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import GenericViewSet
from rest_framework_simplejwt.tokens import RefreshToken

from users_event.models import Event, Participant, Tag, Rating, User
from users_event.serializers import (
    EventInfoSerializer,
    TagSerializer,
    EventDetailSerializer,
    RatingSerializer,
    MeanRatingSerializer,
    ParticipantSerializer,
    ParticipantSerializerForCalendar,
)


class ParticipantViewSetForCalendar(mixins.ListModelMixin, GenericViewSet):
    serializer_class = ParticipantSerializerForCalendar

    def get_queryset(self, *args, **kwargs):
        return Participant.objects.filter(
            Q(user=self.request.user) & Q(is_organizer=False)
        )

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


class ParticipantViewSet(APIView):
    """API для просмотра подписчиков мероприятия"""

    def get(self, request):
        event_id = request.GET["event_id"]
        subscribed_users = Participant.objects.filter(
            Q(event_id=event_id) & Q(is_organizer=False)
        )
        serializer = ParticipantSerializer(subscribed_users, many=True)
        return Response(serializer.data)


class SubscribeViewSet(APIView):
    """API для подписки пользователя на бесплатное мероприятие"""

    def post(self, request):
        event_id = request.data["event"]["id"]
        ans = Participant(user=request.user, event_id=event_id, is_organizer=False)
        ans.save()
        return Response({"message": "Subscribe successful"})


class TagViewSet(mixins.ListModelMixin, mixins.CreateModelMixin, GenericViewSet):
    pagination_class = None
    serializer_class = TagSerializer

    def get_queryset(self):
        return Tag.objects.filter(user=self.request.user)


class RatingViewSet(mixins.CreateModelMixin, mixins.ListModelMixin, GenericViewSet):
    queryset = Rating.objects.all()

    def get_serializer_class(self):
        if self.action == "mean_rate":
            return MeanRatingSerializer
        else:
            return RatingSerializer

    def perform_create(self, serializer):
        serializer.save()

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(serializer.data)

    @action(detail=False, methods=["get"], permission_classes=[IsAuthenticated])
    def mean_rate(self, request, *args, **kwargs):
        event_id = self.request.GET["event_id"]
        avg_rating = Rating.objects.filter(event=event_id).aggregate(Avg("rating"))[
            "rating__avg"
        ]
        print(avg_rating)
        serializer = self.get_serializer({"rate": avg_rating})
        return Response(serializer.data)


class EventViewSet(
    mixins.RetrieveModelMixin,
    # mixins.UpdateModelMixin,
    # mixins.DestroyModelMixin,
    mixins.ListModelMixin,
    GenericViewSet,
):
    def get_serializer_class(self):
        if self.action in ("retrieve", "list"):
            return EventDetailSerializer
        else:
            return EventInfoSerializer

    def get_queryset(self, *args, **kwargs):
        if "slug" in self.request.GET.keys():
            category = self.request.GET["slug"]
            return Event.objects.filter(category=category)
        else:
            return Event.objects.all()

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, user_id=request.user.id)
        return Response(serializer.data)


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

    def converting_data(self, request):
        """
        Создает новый тег, если его не существует и
        заменяет значения price и url на null
        :param request:
        :type request:
        :return:
        :rtype:
        """
        price = request.POST.get("price")
        if price == "null":
            price = None
        else:
            price = int(price)
        url = request.POST.get("url")
        if url == "null":
            url = None
        tag_names = request.data.getlist("tags")
        print(request.data)
        tags = []
        for tag_request in tag_names:
            tag = Tag.objects.filter(title=tag_request).first()
            if tag is None:
                tag = self.create_new_tag(request, tag_request)
            tags.append(tag.title)
        event_data = request.data.dict()
        event_data["tags"] = tags
        event_data["price"] = price
        event_data["url"] = url
        return event_data

    def create(self, request, *args, **kwargs):
        event_data = self.converting_data(request)
        serializer = self.get_serializer(data=event_data)
        serializer.is_valid(raise_exception=True)
        event = self.perform_create(serializer)
        ans = Participant(user=request.user, event=event, is_organizer=True)
        ans.save()
        return Response(serializer.data)

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop("partial", False)
        instance = self.get_object()
        serializer = self.get_serializer(
            instance, data=self.converting_data(request), partial=partial
        )
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        if getattr(instance, "_prefetched_objects_cache", None):
            instance._prefetched_objects_cache = {}

        return Response(serializer.data)

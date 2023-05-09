from django.db.models import Q
from django.utils import timezone
from rest_framework import serializers

from users_event.models import Event, Tag, Rating, Participant


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = "__all__"


class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = "__all__"


class MeanRatingSerializer(serializers.Serializer):
    rate = serializers.FloatField()


class ParticipantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Participant
        fields = "__all__"


class ParticipantSerializerForCalendar(ParticipantSerializer):
    event = serializers.SerializerMethodField()

    def get_event(self, obj):
        event = Event.objects.filter(id=obj.event_id).first()
        serializer = EventDetailSerializerForCalendar(event)
        return serializer.data


class EventInfoSerializer(serializers.ModelSerializer):
    """Сериализатор, для редактирвования и добавления мероприятия"""

    tags = serializers.SlugRelatedField(
        many=True, read_only=False, slug_field="title", queryset=Tag.objects.all()
    )

    class Meta:
        model = Event
        fields = "__all__"


class CustomDateTimeField(serializers.DateTimeField):
    """Сериализатор для отображения времени на экране для пользователей"""

    def to_representation(self, value):
        value = timezone.localtime(value)
        return value.strftime("%Y-%m-%d %H:%M:%S")


class CustomDateTimeFieldForCalendar(serializers.DateTimeField):
    """Сериализатор для отображения времени на календаре для пользователей"""

    def to_representation(self, value):
        value = timezone.localtime(value)
        return value.strftime("%Y-%m-%d")


class EventDetailSerializer(EventInfoSerializer):
    """Сериализатор, для получения детальной (полной) информации о мероприятии и для вывода информации на карточках"""

    start_time = CustomDateTimeField()
    finish_time = CustomDateTimeField()
    rating_event = serializers.SerializerMethodField()
    organizer = serializers.SerializerMethodField()

    def __init__(self, *args, **kwargs):
        user_id = kwargs.pop("user_id", None)
        super().__init__(*args, **kwargs)
        self.user_id = user_id

    # def get_start_time(self, event):
    #     return event.start_time.strftime("%Y-%m-%d %H:%M")
    #
    # def get_finish_time(self, event):
    #     return event.finish_time.strftime("%Y-%m-%d %H:%M")

    def get_rating_event(self, event):
        qs = Rating.objects.filter(event=event)
        if self.user_id:
            qs.filter(user_id=self.user_id)
        serializer = RatingSerializer(qs, many=True)
        return serializer.data

    def get_organizer(self, event):
        qs = Participant.objects.filter(Q(event=event) & Q(is_organizer=True))
        serializer = ParticipantSerializer(qs, many=True)
        return serializer.data


class EventDetailSerializerForCalendar(EventDetailSerializer):
    start_time = CustomDateTimeFieldForCalendar()
    finish_time = CustomDateTimeFieldForCalendar()
    # def get_start_time(self, event):
    #     return event.start_time.strftime("%Y-%m-%d")
    #
    # def get_finish_time(self, event):
    #     return event.finish_time.strftime("%Y-%m-%d")

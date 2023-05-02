from django.db.models import Q
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


class EventInfoSerializer(serializers.ModelSerializer):
    """Сериализатор, для редактирвования и добавления мероприятия"""

    tags = serializers.SlugRelatedField(
        many=True, read_only=False, slug_field="title", queryset=Tag.objects.all()
    )

    class Meta:
        model = Event
        fields = "__all__"


class EventDetailSerializer(EventInfoSerializer):
    """Сериализатор, для получения детальной (полной) информации о мероприятии"""

    start_time = serializers.SerializerMethodField()
    finish_time = serializers.SerializerMethodField()
    rating_event = serializers.SerializerMethodField()
    organizer = serializers.SerializerMethodField()

    def __init__(self, *args, **kwargs):
        user_id = kwargs.pop("user_id", None)
        super().__init__(*args, **kwargs)
        self.user_id = user_id

    def get_start_time(self, event):
        return event.start_time.strftime("%Y-%m-%d %H:%M")

    def get_finish_time(self, event):
        return event.finish_time.strftime("%Y-%m-%d %H:%M")

    def get_rating_event(self, event):
        qs = Rating.objects.filter(event=event)
        if self.user_id:
            qs.filter(user_id=self.user_id)
        serializer = RatingSerializer(qs, many=True)
        return serializer.data

    def get_organizer(self, event):
        qs = Participant.objects.filter(event=event)
        if self.user_id:
            qs.filter(Q(is_organizer=True) & Q(user=self.user_id))
        serializer = ParticipantSerializer(qs, many=True)
        return serializer.data

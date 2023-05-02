from rest_framework import serializers

from users_event.models import Event, Tag, Rating


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = "__all__"


class EventInfoSerializer(serializers.ModelSerializer):
    tags = serializers.SlugRelatedField(
        many=True, read_only=False, slug_field="title", queryset=Tag.objects.all()
    )

    class Meta:
        model = Event
        fields = "__all__"


class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = ("user_id", "rating")


class EventDetailSerializer(EventInfoSerializer):
    rating_event = serializers.SerializerMethodField()

    def __init__(self, *args, **kwargs):
        user_id = kwargs.pop("user_id", None)
        super().__init__(*args, **kwargs)
        self.user_id = user_id

    def get_rating_event(self, event):
        print(event)
        qs = Rating.objects.filter(event=event)
        if self.user_id:
            qs.filter(user_id=self.user_id)
        serializer = RatingSerializer(qs, many=True)
        return serializer.data

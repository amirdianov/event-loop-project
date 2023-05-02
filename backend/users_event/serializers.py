from rest_framework import serializers

from users_event.models import Event, Tag


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

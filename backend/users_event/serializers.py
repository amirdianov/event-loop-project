from rest_framework import serializers

from users_event.models import Event, Tag


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ("id", "title")


class EventInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = "__all__"

from rest_framework import serializers

from comments_system.models import Comment
from users_event.serializers import CustomDateTimeField


class CommentInfoSerializer(serializers.ModelSerializer):
    user_name = serializers.CharField(source="user.name", read_only=True)
    created_at = CustomDateTimeField()

    class Meta:
        model = Comment
        fields = ("created_at", "text", "user_name")


class CommentCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ("user", "text", "created_at", "event")

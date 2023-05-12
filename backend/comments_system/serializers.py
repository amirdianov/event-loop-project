from rest_framework import serializers

from authorisation_token.serializers import UserProfileSerializer
from comments_system.models import Comment, User


class CommentSerializer(serializers.ModelSerializer):
    user_name = serializers.CharField(source="user.name", read_only=True)

    class Meta:
        model = Comment
        fields = ("created_at", "text", "user_name")

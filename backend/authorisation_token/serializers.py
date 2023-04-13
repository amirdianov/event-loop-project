from rest_framework import serializers

from authorisation_token.models import User


class StatusCheckSerializer(serializers.Serializer):
    status = serializers.CharField()
    user_id = serializers.IntegerField()


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"


class UserFormSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()


class TokensSerializer(serializers.Serializer):
    refresh = serializers.CharField()
    access = serializers.CharField()

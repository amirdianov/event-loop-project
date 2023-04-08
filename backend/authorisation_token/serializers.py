from rest_framework import serializers


class StatusCheckSerializer(serializers.Serializer):
    status = serializers.CharField()
    user_id = serializers.IntegerField()

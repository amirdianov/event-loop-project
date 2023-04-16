import requests
from django.contrib.auth import authenticate
from rest_framework.decorators import api_view, permission_classes
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.response import Response

from authorisation_token.serializers import (
    StatusCheckSerializer,
    UserFormSerializer,
    TokensSerializer,
    UserProfileSerializer,
)


# Create your views here.
@api_view()
def status_view(request):
    return Response(
        StatusCheckSerializer({"status": "ok", "user_id": request.user.id}).data
    )


@api_view(["GET"])
def profile_view(request):
    profile = UserProfileSerializer(request.user)
    return Response(profile.data)

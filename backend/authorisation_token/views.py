import requests
from django.contrib.auth import authenticate
from rest_framework.decorators import api_view, permission_classes
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.response import Response

from authorisation_token.serializers import (
    StatusCheckSerializer,
    UserSerializer,
    UserFormSerializer,
    TokensSerializer,
)


# Create your views here.
@api_view()
def status_view(request):
    return Response(
        StatusCheckSerializer({"status": "ok", "user_id": request.user.id}).data
    )


@api_view(["POST"])
@permission_classes([])
def auth_view(request):
    data = UserFormSerializer(data=request.data)
    data.is_valid(raise_exception=True)
    user = authenticate(request, **data.validated_data)
    if user is None:
        raise AuthenticationFailed()
    else:
        tokens = requests.post(
            "http://127.0.0.1:8000/api/token/",
            data={"email": request.data["email"], "password": request.data["password"]},
        )
        # print(tokens.json())
        tokens = TokensSerializer(tokens.json())
        return Response(tokens.data)


@api_view(["GET"])
def profile_view(request):
    if not request.user.is_anonymous:
        serializer = UserSerializer(request.user)
        return Response(serializer.data)
    else:
        return Response(StatusCheckSerializer({"status": "bad", "user_id": 404}).data)

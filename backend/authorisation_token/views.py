from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework_simplejwt.tokens import RefreshToken

from authorisation_token.models import User
from authorisation_token.serializers import (
    StatusCheckSerializer,
    UserProfileSerializer,
    UserRegistrationSerializer,
    TokensSerializer,
)


def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)

    return {
        "refresh": str(refresh),
        "access": str(refresh.access_token),
    }


# Create your views here.
@api_view()
@permission_classes([])
def status_view(request):
    return Response(
        StatusCheckSerializer({"status": "ok", "user_id": request.user.id}).data
    )


@api_view(["GET"])
def profile_view(request):
    profile = UserProfileSerializer(request.user)
    return Response(profile.data)


@api_view(["POST"])
@permission_classes([])
def registration_view(request):
    user_info = UserRegistrationSerializer(data=request.data)
    user_info.is_valid(raise_exception=True)
    user_info = dict(user_info.validated_data)
    user = User(
        name=user_info["name"], surname=user_info["surname"], email=user_info["email"]
    )
    user.set_password(user_info["password"])
    user.save()
    tokens = get_tokens_for_user(user)
    return Response(TokensSerializer(tokens).data)


class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserProfileSerializer

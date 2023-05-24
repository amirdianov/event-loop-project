import requests
from django.conf import settings
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.core.mail import EmailMessage
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from drf_yasg.utils import swagger_auto_schema
from rest_framework import mixins, status
from rest_framework.decorators import action, api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet
from rest_framework_simplejwt.tokens import RefreshToken

from authorisation_token.models import User
from authorisation_token.serializers import (
    StatusCheckSerializer,
    UserProfileSerializer,
    UserRegistrationSerializer,
    TokensSerializer,
    PasswordSerializer,
)
from eventloop.settings import CLIENT_ID_YANDEX, CLIENT_SECRET_YANDEX


def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)

    return {
        "refresh": str(refresh),
        "access": str(refresh.access_token),
    }


# Create your views here.
@swagger_auto_schema(method="GET", operation_id="api_status")
@api_view()
@permission_classes([])
def status_view(request):
    return Response(
        StatusCheckSerializer({"status": "ok", "user_id": request.user.id}).data
    )


class UserViewSet(
    mixins.UpdateModelMixin,
    mixins.ListModelMixin,
    GenericViewSet,
):
    queryset = User.objects.all()
    serializer_class = UserProfileSerializer

    @action(
        detail=False,
        methods=["post"],
        permission_classes=[],
        url_name="registration",
        url_path="registration",
    )
    def registration(self, request, pk=None):
        user_info = UserRegistrationSerializer(data=request.data)
        user_info.is_valid(raise_exception=True)
        user_info = dict(user_info.validated_data)
        user = User(
            name=user_info["name"],
            surname=user_info["surname"],
            email=user_info["email"],
        )
        user.set_password(user_info["password"])
        user.save()
        tokens = get_tokens_for_user(user)
        return Response(TokensSerializer(tokens).data)

    @action(
        detail=False,
        methods=["get"],
        permission_classes=[IsAuthenticated],
        url_name="profile",
        url_path="profile",
    )
    def profile(self, request, pk=None):
        profile = UserProfileSerializer(request.user)
        return Response(profile.data)

    @action(
        detail=True,
        methods=["post"],
        permission_classes=[IsAuthenticated],
        url_name="set_password",
        url_path="set_password",
    )
    def set_password(self, request, pk):
        user = self.get_object()
        serializer = PasswordSerializer(data=request.data)
        if serializer.is_valid():
            user.set_password(serializer.validated_data["password"])
            user.save()
            profile = UserProfileSerializer(user)
            return Response(profile.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["POST"])
@permission_classes([])
def forgot_password_view(request):
    email = request.data["email"]
    user = User.objects.get(email=email)

    token_generator = PasswordResetTokenGenerator()
    token = token_generator.make_token(user)

    uidb64 = urlsafe_base64_encode(force_bytes(user.pk))
    reset_url = f"http://localhost:5173/reset_password/{uidb64}/{token}/"
    email = EmailMessage(
        "Сброс пароля",
        reset_url,
        settings.DEFAULT_FROM_EMAIL,
        [email],
    )
    email.send()
    return Response({"status": "ok"})


@api_view(["POST"])
@permission_classes([])
def reset_password_view(request):
    token = request.data["token"]
    uid = request.data["uid"]
    try:
        uid = urlsafe_base64_decode(uid).decode("utf-8")
        user = User.objects.get(id=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and PasswordResetTokenGenerator().check_token(user, token):
        password = request.data["password"]
        user.set_password(password)
        user.save()
        return Response({"status": "ok"})
    else:
        return Response(
            {"status": "error", "message": "Ошибка"}, status=status.HTTP_400_BAD_REQUEST
        )


@api_view(["POST"])
@permission_classes([])
def yandex_token_view(request):
    print("я тут")
    code = request.data["code"]

    data = {
        "grant_type": "authorization_code",
        "code": code,
        "client_id": CLIENT_ID_YANDEX,
        "client_secret": CLIENT_SECRET_YANDEX,
        "redirect_uri": "http://localhost:5173/",
    }
    print(data)
    token = requests.post(
        url="https://oauth.yandex.ru/token",
        headers={"Content-Type": "application/x-www-form-urlencoded"},
        data=data,
    )
    print(token.json())
    user_info = requests.get(
        f'https://login.yandex.ru/info?oauth_token={token.json()["access_token"]}'
    ).json()
    user = User(name=user_info["display_name"], email=user_info["emails"][0])
    try:
        user.save()
    except:
        user = User.objects.filter(email=user_info["emails"][0]).first()
    refresh = RefreshToken.for_user(user)
    access = refresh.access_token
    return Response({"refresh": str(refresh), "access": str(access)})

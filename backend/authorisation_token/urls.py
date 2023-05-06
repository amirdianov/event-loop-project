from django.urls import path, include
from rest_framework.routers import SimpleRouter
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)

from authorisation_token.views import (
    status_view,
    UserViewSet,
    yandex_token_view,
    forgot_password_view,
    reset_password_view,
)

users_router = SimpleRouter()
users_router.register("users", UserViewSet, basename="users")

urlpatterns = [
    path("", status_view, name="status"),
    path("token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("token/verify/", TokenVerifyView.as_view(), name="token_verify"),
    path("", include(users_router.urls)),
    path("yandex_token/", yandex_token_view, name="yandex_token"),
    path("forgot_password/", forgot_password_view, name="forgot_password"),
    path("reset_password/", reset_password_view, name="reset_password"),
]

from django.urls import path
from rest_framework.routers import SimpleRouter
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)

from authorisation_token.views import (
    status_view,
    profile_view,
    registration_view,
    UserViewSet,
)

router = SimpleRouter()
router.register("users", UserViewSet, basename="users")

urlpatterns = [
    path("", status_view, name="status"),
    path("token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("token/verify/", TokenVerifyView.as_view(), name="token_verify"),
    path("profile/", profile_view, name="profile"),
    path("registration/", registration_view, name="registration"),
] + router.urls

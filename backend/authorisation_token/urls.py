from django.urls import path, include
from rest_framework.routers import SimpleRouter

from authorisation_token.views import status_view, UserViewSet

router = SimpleRouter()
router.register("users", UserViewSet, basename="users")
urlpatterns = [
    path("drf-auth/", include("rest_framework.urls")),
    path("", status_view, name="status"),
] + router.urls

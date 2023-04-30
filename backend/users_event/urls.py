from django.urls import path, include
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework.routers import SimpleRouter
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)

from authorisation_token.views import (
    status_view,
)
from users_event.views import EventViewSet, UserEventViewSet, TagViewSet

users_router = SimpleRouter()
users_router.register("events", EventViewSet, basename="events")
users_router.register("my_events", UserEventViewSet, basename="my_events")
users_router.register("tags", TagViewSet, basename="tags")

urlpatterns = [
    path("", status_view, name="status"),
    path("", include(users_router.urls)),
]

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
from users_event.views import EventViewSet

users_router = SimpleRouter()
users_router.register("events", EventViewSet, basename="events")

schema_view = get_schema_view(
    openapi.Info(
        title="Events API",
        default_version="v1",
        description="Event-loop project",
        contact=openapi.Contact(email="event-loop@gmail.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=[],
)
urlpatterns = [
    path("", status_view, name="status"),
    path("", include(users_router.urls)),
]

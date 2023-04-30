from django.urls import path, include
from rest_framework.routers import SimpleRouter

from authorisation_token.views import (
    status_view,
)
from users_event.views import EventViewSet, UserEventViewSet, TagViewSet

users_router = SimpleRouter()
users_router.register("events", EventViewSet, basename="events")
events_router = SimpleRouter()
events_router.register("my_events", UserEventViewSet, basename="my_events")
tags_router = SimpleRouter()
tags_router.register("tags", TagViewSet, basename="tags")

urlpatterns = [
    path("", status_view, name="status"),
    path("", include(users_router.urls)),
    path("", include(events_router.urls)),
    path("", include(tags_router.urls)),
]

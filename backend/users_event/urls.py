from django.urls import path, include
from rest_framework.routers import SimpleRouter

from authorisation_token.views import (
    status_view,
)
from users_event.views import (
    EventViewSet,
    UserEventViewSet,
    TagViewSet,
    RatingViewSet,
    SubscribeViewSet,
    ParticipantViewSet,
    ParticipantViewSetForCalendar,
    pay_event_view,
    get_pk_view,
    pay_event_response_view,
    # confirm_payment_view,
    # hello_world,
)

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
    path(
        "rate/",
        RatingViewSet.as_view({"post": "create", "get": "mean_rate"}),
        name="rate",
    ),
    path("subscribe/", SubscribeViewSet.as_view(), name="subscribe"),
    path("subscribers/", ParticipantViewSet.as_view(), name="subscribers"),
    path(
        "user_subscriptions/",
        ParticipantViewSetForCalendar.as_view({"get": "list"}),
        name="subscriptions",
    ),
    path("pay_event/", pay_event_view, name="pay_event"),
    path("get_pk/", get_pk_view, name="get_pk_view"),
    path("pay_event_response/", pay_event_response_view, name="pay_event_response"),
]

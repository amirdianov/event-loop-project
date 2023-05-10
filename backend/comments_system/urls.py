from django.urls import path

from authorisation_token.views import (
    status_view,
)

urlpatterns = [
    path("", status_view, name="status"),
]

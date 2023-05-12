from django.urls import path

from authorisation_token.views import (
    status_view,
)
from comments_system.views import CommentView

urlpatterns = [
    path("", status_view, name="status"),
    path(
        "event_comments/",
        CommentView.as_view({"get": "list", "post": "create"}),
        name="comments",
    ),
]

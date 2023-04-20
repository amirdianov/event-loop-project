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
    UserViewSet,
)

users_router = SimpleRouter()
users_router.register("users", UserViewSet, basename="users")

schema_view = get_schema_view(
    openapi.Info(
        title="Users API",
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
    path("token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("token/verify/", TokenVerifyView.as_view(), name="token_verify"),
    path(
        "swagger/",
        schema_view.with_ui("swagger", cache_timeout=0),
        name="schema-swagger-ui",
    ),
    path("", include(users_router.urls)),
]

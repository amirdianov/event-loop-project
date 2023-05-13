from django.urls import path

from comments_system.consumers import MainConsumer

websocket_urlpatterns = [path("ws/server/<str:room>/", MainConsumer.as_asgi())]

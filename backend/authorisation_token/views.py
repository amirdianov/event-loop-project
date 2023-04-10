import time

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from authorisation_token.models import User
from authorisation_token.serializers import StatusCheckSerializer, UserSerializer


# Create your views here.
@api_view()
def status_view(request):
    # time.sleep(3)
    return Response(
        StatusCheckSerializer({"status": "ok", "user_id": request.user.id}).data
    )


class UserViewSet(ModelViewSet):
    queryset = User.object.all()
    serializer_class = UserSerializer

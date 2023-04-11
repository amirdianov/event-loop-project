from rest_framework.decorators import api_view
from rest_framework.response import Response

from authorisation_token.serializers import StatusCheckSerializer, UserSerializer


# Create your views here.
@api_view()
def status_view(request):
    # time.sleep(3)
    return Response(
        StatusCheckSerializer({"status": "ok", "user_id": request.user.id}).data
    )


@api_view(["GET"])
def profile_view(request):
    if not request.user.is_anonymous:
        serializer = UserSerializer(request.user)
        return Response(serializer.data)
    else:
        return Response(StatusCheckSerializer({"status": "bad", "user_id": 404}).data)

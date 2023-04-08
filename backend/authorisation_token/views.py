import time

from rest_framework.decorators import api_view
from rest_framework.response import Response

from authorisation_token.serializers import StatusCheckSerializer


# Create your views here.
@api_view()
def status_view(request):
    time.sleep(3)
    return Response(
        StatusCheckSerializer({"status": "ok", "user_id": request.user.id}).data
    )

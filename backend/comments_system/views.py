from rest_framework import mixins
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from comments_system.models import Comment
from comments_system.serializers import CommentSerializer


# Create your views here.


class CommentView(mixins.CreateModelMixin, mixins.ListModelMixin, GenericViewSet):
    serializer_class = CommentSerializer

    def get_queryset(self, *args, **kwargs):
        return Comment.objects.filter(event_id=kwargs["event_id"])

    def list(self, request, *args, **kwargs):
        print(request.GET["event_id"])
        queryset = self.filter_queryset(
            self.get_queryset(event_id=request.GET["event_id"])
        )
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

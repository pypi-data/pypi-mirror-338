from rest_framework import serializers, status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView
from sparkplug_core.utils import get_object

from ..models import Notification
from ..permissions import RecipientPermission


class SetStarView(APIView):
    """Sets the `is_starred` field for a notification."""

    permission_classes = (RecipientPermission,)

    class InputSerializer(serializers.Serializer):
        is_starred = serializers.BooleanField()

    def patch(self, request: Request, uuid: str) -> Response:
        notification = get_object(Notification, uuid=uuid)

        self.check_object_permissions(request, notification)

        serializer = self.InputSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        notification.is_starred = serializer.validated_data["is_starred"]
        notification.save()

        return Response(status=status.HTTP_204_NO_CONTENT)

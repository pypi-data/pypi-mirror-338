from rest_framework import serializers, status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView
from sparkplug_core.permissions import AuthPermission

from .. import services


class MarkReadView(APIView):
    """Marks notifications as read."""

    permission_classes = (AuthPermission,)

    class InputSerializer(serializers.Serializer):
        uuids = serializers.ListField(
            child=serializers.CharField(),
        )

    def patch(self, request: Request) -> Response:
        serializer = self.InputSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        services.mark_read(
            user=request.user,
            uuids=serializer.validated_data["uuids"],
        )
        return Response(status=status.HTTP_204_NO_CONTENT)

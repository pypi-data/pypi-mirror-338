from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView
from sparkplug_core.permissions import AuthPermission
from sparkplug_core.utils import get_paginated_response

from ..filters import list_filter
from ..queries import notifications_list
from ..serializers import DetailSerializer


class ListView(APIView):
    permission_classes = (AuthPermission,)

    def get(self, request: Request) -> Response:
        filters = list_filter(
            recipient=request.user,
            is_starred=request.query_params.get("is_starred"),
        )

        queryset = (
            notifications_list(filters)
            .order_by("-created")
            .prefetch_related("recipient")
            .prefetch_related("actor")
        )

        return get_paginated_response(
            serializer_class=DetailSerializer,
            queryset=queryset,
            request=request,
            view=self,
        )

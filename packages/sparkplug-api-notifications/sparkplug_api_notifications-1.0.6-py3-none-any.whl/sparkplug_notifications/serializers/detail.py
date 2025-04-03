import importlib

from django.conf import settings
from rest_framework.serializers import ModelSerializer
from sparkplug_core.fields import UserUuidField

from ..models import Notification


def get_class(target: str):  # noqa: ANN201
    module_name, class_name = target.rsplit(".", 1)
    module = importlib.import_module(module_name)
    return getattr(module, class_name)


UserTeaser = get_class(settings.USER_TEASER)


class DetailSerializer(
    ModelSerializer["Notification"],
):
    actor_uuid = UserUuidField(source="actor")
    actor = UserTeaser()

    class Meta:
        model = Notification

        fields = (
            "uuid",
            "created",
            "actor_uuid",
            "actor",
            "actor_text",
            "has_read",
            "is_starred",
            "message",
            "target_route",
        )

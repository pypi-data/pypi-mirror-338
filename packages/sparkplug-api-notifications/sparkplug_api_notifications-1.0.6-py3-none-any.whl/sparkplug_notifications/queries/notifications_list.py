from django.db.models import QuerySet

from ..filters import ListFilter
from ..models import Notification


def notifications_list(
    filters: ListFilter,
) -> QuerySet["Notification"]:
    filter_kwargs = filters.model_dump(exclude_none=True)
    return Notification.objects.filter(**filter_kwargs)

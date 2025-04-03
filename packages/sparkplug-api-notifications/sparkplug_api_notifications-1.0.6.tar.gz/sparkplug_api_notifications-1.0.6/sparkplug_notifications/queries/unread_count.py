from django.contrib.auth.base_user import AbstractBaseUser
from django.db.models import QuerySet

from ..filters import list_filter
from ..models import Notification
from ..queries import notifications_list


def unread_count(
    recipient: type[AbstractBaseUser],
) -> QuerySet["Notification"]:
    filters = list_filter(
        recipient=recipient,
        has_read=False,
    )
    return notifications_list(filters).count()

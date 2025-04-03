from django.contrib.auth.base_user import AbstractBaseUser

from ..filters import list_filter
from ..queries import notifications_list


def mark_read(user: type[AbstractBaseUser], uuids: list[str]) -> None:
    filters = list_filter(recipient=user)
    notifications_list(filters).filter(uuid__in=uuids).update(has_read=True)

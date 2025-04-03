from typing import Optional

from django.contrib.auth.base_user import AbstractBaseUser
from pydantic import BaseModel, ValidationError
from rest_framework.exceptions import ValidationError as DRFValidationError


class ListFilter(BaseModel):
    recipient: AbstractBaseUser
    has_read: Optional[bool] = None
    is_starred: Optional[bool] = None

    class Config:
        # Allow arbitrary types like AbstractBaseUser
        arbitrary_types_allowed = True


def list_filter(
    *,
    recipient: AbstractBaseUser,
    has_read: Optional[str] = None,
    is_starred: Optional[str] = None,
) -> ListFilter:
    """
    Helper function to create a ListFilter instance.
    """
    try:
        return ListFilter(
            recipient=recipient,
            has_read=has_read,
            is_starred=is_starred,
        )
    except ValidationError as e:
        raise DRFValidationError(detail=e.errors())

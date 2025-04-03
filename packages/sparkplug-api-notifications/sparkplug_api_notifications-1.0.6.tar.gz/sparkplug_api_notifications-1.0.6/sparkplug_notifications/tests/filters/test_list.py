from apps.users.factories import UserFactory
from django.test import TestCase
from rest_framework.exceptions import ValidationError as DRFValidationError

from sparkplug_notifications.filters.list import list_filter


class TestListFilter(TestCase):
    def setUp(self):
        self.user = UserFactory()

    def test_valid_filter(self):
        # Test with valid inputs
        filter_instance = list_filter(
            recipient=self.user,
            has_read="true",
            is_starred="false",
        )
        assert filter_instance.recipient == self.user
        assert filter_instance.has_read is True
        assert filter_instance.is_starred is False

    def test_invalid_recipient(self):
        # Test with invalid recipient type
        with self.assertRaises(DRFValidationError) as exc_info:
            list_filter(
                recipient="invalid_user",
                has_read="true",
                is_starred="false",
            )
        assert "recipient" in str(exc_info.exception)

    def test_invalid_has_read_value(self):
        # Test with invalid has_read value
        with self.assertRaises(DRFValidationError) as exc_info:
            list_filter(
                recipient=self.user,
                has_read="invalid",
                is_starred="false",
            )
        assert "has_read" in str(exc_info.exception)

    def test_invalid_starred_value(self):
        # Test with invalid starred value
        with self.assertRaises(DRFValidationError) as exc_info:
            list_filter(
                recipient=self.user,
                has_read="true",
                is_starred="invalid",
            )
        assert "starred" in str(exc_info.exception)

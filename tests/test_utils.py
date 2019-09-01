# -*- coding: utf-8 -*-

# django-djcopyright
# tests/test_utils.py


from typing import List  # pylint: disable=W0611

from django.test import TestCase
from django.test.utils import override_settings
from django.utils import timezone

from djcopyright.utils import get_copyright


__all__ = ["GetCopyrightUtilTest"]  # type: List[str]


YEAR = timezone.now().today().year  # type: int


class GetCopyrightUtilTest(TestCase):
    """
    get_copyright util tests.
    """

    @override_settings(DJCOPYRIGHT_START_YEAR=YEAR)
    def test_get_copyright__start_year_equal_current(self) -> None:
        """
        Util must return start year from settings if it equal current year.

        :return: nothing.
        :rtype: None.
        """

        self.assertEqual(first=get_copyright(), second=YEAR)

    @override_settings(DJCOPYRIGHT_SHOW_START_YEAR=False, DJCOPYRIGHT_START_YEAR=1970)
    def test_get_copyright__without_showing_start_year(self) -> None:
        """
        Util must return only current year.

        :return: nothing.
        :rtype: None.
        """

        self.assertEqual(first=get_copyright(), second=YEAR)

    @override_settings(DJCOPYRIGHT_SHOW_CURRENT_YEAR=False, DJCOPYRIGHT_START_YEAR=1970)
    def test_get_copyright__without_showing_current_year(self) -> None:
        """
        Util must return only start year.

        :return: nothing.
        :rtype: None.
        """

        self.assertEqual(first=get_copyright(), second=1970)

    @override_settings(DJCOPYRIGHT_START_YEAR=1970)
    def test_get_copyright__show_all(self) -> None:
        """
        Util must return start and current year.

        :return: nothing.
        :rtype: None.
        """

        self.assertEqual(first=get_copyright(), second=f"1970 - {YEAR}")

    @override_settings(
        DJCOPYRIGHT_START_YEAR=1970,
        DJCOPYRIGHT_FORMAT_STRING="{start_year} — {current_year}",
    )
    def test_get_copyright__show_all__using_custom_format(self) -> None:
        """
        Util must return start and current year using custom format string.

        :return: nothing.
        :rtype: None.
        """

        self.assertEqual(first=get_copyright(), second=f"1970 — {YEAR}")

    @override_settings(DJCOPYRIGHT_START_YEAR=YEAR + 1)
    def test_get_copyright__start_year_greater_than_current(self) -> None:
        """
        Util must return current year.

        :return: nothing.
        :rtype: None.
        """

        self.assertEqual(first=get_copyright(), second=YEAR)

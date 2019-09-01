# -*- coding: utf-8 -*-

# django-djcopyright
# tests/templatetags/test_djcopyright_tags.py


from typing import List  # pylint: disable=W0611

from django.test import TestCase
from django.utils import timezone

from djcopyright.templatetags.djcopyright_tags import djcopyright_years


__all__ = ["DjcopyrightYearsTemplatetagTest"]  # type: List[str]


YEAR = timezone.now().today().year  # type: int


class DjcopyrightYearsTemplatetagTest(TestCase):
    """
    Djcopyright years templatetag tests.
    """

    def test_djcopyright_years(self) -> None:
        """
        Must return formatted copyright tag.

        :return: nothing.
        :rtype: None.
        """

        result = djcopyright_years()  # type: str

        self.assertIsInstance(obj=result, cls=str)
        self.assertEqual(first=result, second=str(YEAR))

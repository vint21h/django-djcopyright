# -*- coding: utf-8 -*-

# django-djcopyright
# tests/templatetags/test_djcopyright_tags.py


from typing import List

from django.test import TestCase
from django.utils import timezone

from djcopyright.templatetags.djcopyright_tags import djcopyright_years


__all__: List[str] = ["DjcopyrightYearsTemplatetagTest"]


YEAR: int = timezone.now().today().year


class DjcopyrightYearsTemplatetagTest(TestCase):
    """Djcopyright years templatetag tests."""

    def test_djcopyright_years(self) -> None:
        """Must return formatted copyright tag."""
        result: str = djcopyright_years()

        self.assertIsInstance(obj=result, cls=str)
        self.assertEqual(first=result, second=str(YEAR))

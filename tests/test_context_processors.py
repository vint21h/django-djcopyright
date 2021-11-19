# -*- coding: utf-8 -*-

# django-djcopyright
# tests/test_context_processors.py


from typing import Dict, List

from django.test import TestCase
from django.utils import timezone
from django.http import HttpRequest

from djcopyright.context_processors import djcopyright_years


__all__: List[str] = ["DjcopyrightYearsContextProcessorTest"]


YEAR: int = timezone.now().today().year


class DjcopyrightYearsContextProcessorTest(TestCase):
    """Djcopyright years context processor tests."""

    def test_djcopyright_years(self) -> None:
        """Must return formatted new context variable with copyright."""
        request: HttpRequest = HttpRequest()
        result: Dict[str, str] = djcopyright_years(request=request)

        self.assertIsInstance(obj=result, cls=dict)
        self.assertDictEqual(d1=result, d2={"COPYRIGHT_YEARS": str(YEAR)})

# -*- coding: utf-8 -*-

# django-djcopyright
# tests/test_context_processors.py


from typing import Dict, List  # pylint: disable=W0611

from django.http import HttpRequest
from django.test import TestCase
from django.utils import timezone

from djcopyright.context_processors import djcopyright_years


__all__ = ["DjcopyrightYearsContextProcessorTest"]  # type: List[str]


YEAR = timezone.now().today().year  # type: int


class DjcopyrightYearsContextProcessorTest(TestCase):
    """
    Djcopyright years context processor tests.
    """

    def test_djcopyright_years(self) -> None:
        """
        Must return formatted new context variable with copyright.

        :return: nothing.
        :rtype: None.
        """

        request = HttpRequest()  # type: HttpRequest
        result = djcopyright_years(request=request)  # type: Dict[str, str]

        self.assertIsInstance(obj=result, cls=dict)
        self.assertDictEqual(d1=result, d2={"COPYRIGHT_YEARS": str(YEAR)})

# -*- coding: utf-8 -*-

# django-djcopyright
# djcopyright/settings.py

from __future__ import unicode_literals

from django.conf import settings

__all__ = [
    "START_YEAR",
    "FORMAT_STRING",
    "SHOW_CURRENT_YEAR",
    "SHOW_START_YEAR",
]


START_YEAR = getattr(settings, "DJCOPYRIGHT_START_YEAR", 1970)
FORMAT_STRING = getattr(settings, "DJCOPYRIGHT_FORMAT_STRING", "{start_year} - {current_year}")
SHOW_CURRENT_YEAR = getattr(settings, "DJCOPYRIGHT_SHOW_CURRENT_YEAR", True)
SHOW_START_YEAR = getattr(settings, "DJCOPYRIGHT_SHOW_START_YEAR", True)

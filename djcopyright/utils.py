# -*- coding: utf-8 -*-

# django-djcopyright
# djcopyright/utils.py

from __future__ import unicode_literals
from datetime import date

from djcopyright.settings import START_YEAR, FORMAT_STRING, SHOW_CURRENT_YEAR, SHOW_START_YEAR

__all__ = ["get_copyright", ]


def get_copyright():
    """
    Return formatted copyright years string.
    """

    current_year = date.today().year

    if START_YEAR == current_year:

        return current_year

    elif not SHOW_START_YEAR:

        return current_year

    elif not SHOW_CURRENT_YEAR:

        return START_YEAR

    elif SHOW_CURRENT_YEAR and SHOW_START_YEAR and START_YEAR < current_year:

        return FORMAT_STRING.format(start_year=START_YEAR, current_year=current_year)

    elif START_YEAR and SHOW_START_YEAR > current_year:

        return START_YEAR

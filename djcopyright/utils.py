# -*- coding: utf-8 -*-

# django-djcopyright
# djcopyright/utils.py


from typing import List  # pylint: disable=W0611

from django.utils import timezone

from djcopyright.conf import settings


__all__ = ["get_copyright"]  # type: List[str]


def get_copyright() -> str:
    """
    Format copyright years string.

    :return: formatted copyright years string
    :rtype: str
    """

    current_year = timezone.now().year  # type: int
    copy = ""

    if settings.DJCOPYRIGHT_START_YEAR == current_year:

        copy = str(current_year)

    elif not settings.DJCOPYRIGHT_SHOW_START_YEAR:

        copy = str(current_year)

    elif not settings.DJCOPYRIGHT_SHOW_CURRENT_YEAR:

        copy = str(settings.DJCOPYRIGHT_START_YEAR)

    elif (
        settings.DJCOPYRIGHT_SHOW_CURRENT_YEAR
        and settings.DJCOPYRIGHT_SHOW_START_YEAR  # noqa: W503
        and settings.DJCOPYRIGHT_START_YEAR < current_year  # noqa: W503
    ):

        return settings.DJCOPYRIGHT_FORMAT_STRING.format(
            start_year=settings.DJCOPYRIGHT_START_YEAR, current_year=current_year
        )

    elif (
        settings.DJCOPYRIGHT_START_YEAR
        and settings.DJCOPYRIGHT_SHOW_START_YEAR  # noqa: W503
        and settings.DJCOPYRIGHT_START_YEAR > current_year  # noqa: W503
    ):

        copy = str(current_year)

    return copy

# -*- coding: utf-8 -*-

# django-djcopyright
# djcopyright/utils.py


from typing import List, Union  # pylint: disable=W0611

from django.utils import timezone

from djcopyright.conf import settings


__all__ = ["get_copyright"]  # type: List[str]


def get_copyright() -> Union[int, str, None]:
    """
    Format copyright years string.

    :return: formatted copyright years string.
    :rtype: Union[int, str, None]
    """

    current_year = timezone.now().year  # type: int

    if settings.DJCOPYRIGHT_START_YEAR == current_year:

        return current_year

    elif not settings.DJCOPYRIGHT_SHOW_START_YEAR:

        return current_year

    elif not settings.DJCOPYRIGHT_SHOW_CURRENT_YEAR:

        return settings.DJCOPYRIGHT_START_YEAR

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

        return current_year

    return None

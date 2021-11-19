# -*- coding: utf-8 -*-

# django-djcopyright
# djcopyright/utils.py


from typing import List

from django.utils import timezone

from djcopyright.conf import settings


__all__: List[str] = ["get_copyright"]


def get_copyright() -> str:  # noqa: CCR001
    """
    Format copyright years string.

    :return: formatted copyright years string
    :rtype: str
    """
    current_year: int = timezone.now().year

    if (
        (settings.DJCOPYRIGHT_START_YEAR == current_year)
        or (not settings.DJCOPYRIGHT_SHOW_START_YEAR)  # noqa: W503
        or (  # noqa: W503
            settings.DJCOPYRIGHT_START_YEAR
            and settings.DJCOPYRIGHT_SHOW_START_YEAR  # noqa: W503
            and settings.DJCOPYRIGHT_START_YEAR > current_year  # noqa: W503
        )
    ):
        copyright_ = str(current_year)

    elif not settings.DJCOPYRIGHT_SHOW_CURRENT_YEAR:
        copyright_ = str(settings.DJCOPYRIGHT_START_YEAR)

    elif (
        settings.DJCOPYRIGHT_SHOW_CURRENT_YEAR
        and settings.DJCOPYRIGHT_SHOW_START_YEAR  # noqa: W503
        and settings.DJCOPYRIGHT_START_YEAR < current_year  # noqa: W503
    ):
        copyright_ = settings.DJCOPYRIGHT_FORMAT_STRING.format(
            start_year=settings.DJCOPYRIGHT_START_YEAR, current_year=current_year
        )
    else:
        copyright_ = ""

    return copyright_  # noqa: R504

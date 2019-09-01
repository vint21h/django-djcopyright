# -*- coding: utf-8 -*-

# django-read-only-admin
# djcopyright/conf.py


from typing import List  # pylint: disable=W0611

from appconf import AppConf
from django.conf import settings


__all__ = ["settings"]  # type: List[str]


class DjangoReadOnlyAdminAppConf(AppConf):
    """
    Django read only admin settings.
    """

    START_YEAR = getattr(settings, "DJCOPYRIGHT_START_YEAR", 1970)  # type: int
    FORMAT_STRING = getattr(
        settings, "DJCOPYRIGHT_FORMAT_STRING", "{start_year} - {current_year}"
    )  # type: str
    SHOW_CURRENT_YEAR = getattr(
        settings, "DJCOPYRIGHT_SHOW_CURRENT_YEAR", True
    )  # type: bool
    SHOW_START_YEAR = getattr(
        settings, "DJCOPYRIGHT_SHOW_START_YEAR", True
    )  # type: bool

    class Meta:

        prefix = "djcopyright"  # type: str

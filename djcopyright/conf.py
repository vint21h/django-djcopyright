# -*- coding: utf-8 -*-

# django-djcopyright
# djcopyright/conf.py


from typing import List

from appconf import AppConf
from django.conf import settings


__all__: List[str] = ["settings"]


class DjangoDjcopyrightAppConf(AppConf):
    """Django djcopyright settings."""

    START_YEAR: str = getattr(settings, "DJCOPYRIGHT_START_YEAR", 1970)
    FORMAT_STRING: str = getattr(
        settings,
        "DJCOPYRIGHT_FORMAT_STRING",
        "{start_year} - {current_year}",  # noqa: FS003,E501
    )
    SHOW_CURRENT_YEAR: bool = getattr(settings, "DJCOPYRIGHT_SHOW_CURRENT_YEAR", True)
    SHOW_START_YEAR: bool = getattr(settings, "DJCOPYRIGHT_SHOW_START_YEAR", True)

    class Meta:
        """Config settings."""

        prefix: str = "djcopyright"

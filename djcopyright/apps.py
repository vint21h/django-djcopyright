# -*- coding: utf-8 -*-

# django-djcopyright
# djcopyright/apps.py


from typing import List  # pylint: disable=W0611

from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


__all__ = ["DjangoDjcopyrightConfig"]  # type: List[str]


class DjangoDjcopyrightConfig(AppConfig):
    """
    Application config.
    """

    name = "djcopyright"  # type: str
    verbose_name = _("Django copyright")  # type: str

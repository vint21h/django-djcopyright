# -*- coding: utf-8 -*-

# django-djcopyright
# djcopyright/apps.py


from typing import List

from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


__all__: List[str] = ["DjangoDjcopyrightConfig"]


class DjangoDjcopyrightConfig(AppConfig):
    """Application config."""

    name: str = "djcopyright"
    verbose_name: str = _("Django copyright")

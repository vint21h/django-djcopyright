# -*- coding: utf-8 -*-

# django-djcopyright
# djcopyright/apps.py

from __future__ import unicode_literals

from django.apps import AppConfig

__all__ = ["CopyrightConfig", ]


class CopyrightConfig(AppConfig):

    name = "djcopyright"
    verbose_name = "Django copyright"

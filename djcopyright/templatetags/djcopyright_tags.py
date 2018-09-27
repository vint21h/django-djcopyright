# -*- coding: utf-8 -*-

# django-djcopyright
# djcopyright/templatetags/djcopyright_tags.py


from __future__ import unicode_literals

from django import template

from djcopyright.utils import get_copyright


__all__ = [
    "djcopyright_years",
]


register = template.Library()


@register.simple_tag()
def djcopyright_years():
    """
    Formatted copyright years string templatetag.

    Returns:
        str: formatted copyright years string.
    """

    return get_copyright()

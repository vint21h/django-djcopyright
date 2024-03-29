# -*- coding: utf-8 -*-

# django-djcopyright
# djcopyright/templatetags/djcopyright_tags.py


from typing import List

from django import template

from djcopyright.utils import get_copyright


__all__: List[str] = ["djcopyright_years"]


register = template.Library()


@register.simple_tag()
def djcopyright_years() -> str:
    """
    Format copyright years string templatetag.

    :return: formatted copyright years string
    :rtype: str
    """
    return get_copyright()

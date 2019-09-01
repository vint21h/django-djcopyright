# -*- coding: utf-8 -*-

# django-djcopyright
# djcopyright/templatetags/djcopyright_tags.py


from typing import List, Union  # pylint: disable=W0611

from django import template

from djcopyright.utils import get_copyright


__all__ = ["djcopyright_years"]  # type: List[str]


register = template.Library()


@register.simple_tag()
def djcopyright_years() -> Union[int, str, None]:
    """
    Format copyright years string templatetag.

    :return: formatted copyright years string.
    :rtype: Union[int, str, None]
    """

    return get_copyright()

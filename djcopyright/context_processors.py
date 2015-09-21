# -*- coding: utf-8 -*-

# django-djcopyright
# djcopyright/context_processors.py

from __future__ import unicode_literals

from djcopyright.utils import get_copyright

__all__ = ["djcopyright_years", ]


def djcopyright_years(request):
    """
    Return formatted copyright years string named as 'COPYRIGHT_YEARS' to context.
    """

    return {
        "COPYRIGHT_YEARS": get_copyright(),
    }

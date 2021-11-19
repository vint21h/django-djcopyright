# -*- coding: utf-8 -*-

# django-djcopyright
# djcopyright/context_processors.py


from typing import Dict, List

from django.http import HttpRequest

from djcopyright.utils import get_copyright


__all__: List[str] = ["djcopyright_years"]


def djcopyright_years(request: HttpRequest) -> Dict[str, str]:
    """
    Return formatted copyright years string named as "COPYRIGHT_YEARS" to context.

    :param request: django HTTP request object
    :type request: HttpRequest
    :return: formatted copyright years string named as "COPYRIGHT_YEARS"
    :rtype: Dict[str, str]
    """
    return {"COPYRIGHT_YEARS": get_copyright()}

# -*- coding: utf-8 -*-

# django-djcopyright
# djcopyright/context_processors.py


from typing import Dict, List, Union  # pylint: disable=W0611

from django.http import HttpRequest

from djcopyright.utils import get_copyright


__all__ = ["djcopyright_years"]  # type: List[str]


def djcopyright_years(request: HttpRequest) -> Dict[str, Union[int, str, None]]:
    """
    Return formatted copyright years string named as "COPYRIGHT_YEARS" to context.

    :param request: django HTTP request object.
    :type request: django.http.request.HttpRequest.
    :return: formatted copyright years string named as "COPYRIGHT_YEARS" to context.
    :rtype: Dict[str,  Union[int, str, None]].
    """

    return {"COPYRIGHT_YEARS": get_copyright()}

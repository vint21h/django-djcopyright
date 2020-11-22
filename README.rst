.. django-djcopyright
.. README.rst


A django-djcopyright documentation
==================================

|Travis|_ |Coveralls|_ |Requires|_ |pypi-license|_ |pypi-version|_ |pypi-python-version|_ |pypi-django-version|_ |pypi-format|_ |pypi-wheel|_ |pypi-status|_

    *django-djcopyright is a Django reusable application to show pretty formatted copyright years*

.. contents::

Installation
------------
* Obtain your copy of source code from the git repository: ``$ git clone https://github.com/vint21h/django-djcopyright.git``. Or download the latest release from https://github.com/vint21h/django-djcopyright/tags/.
* Run ``$ python ./setup.py install`` from the repository source tree or unpacked archive. Or use pip: ``$ pip install django-djcopyright``.

Configuration
-------------
* Add ``"djcopyright"`` to ``settings.INSTALLED_APPS``.

.. code-block:: python

    # settings.py

    INSTALLED_APPS += [
        "djcopyright",
    ]

Settings
--------
``DJCOPYRIGHT_START_YEAR``
    Contains year to start show copyright from. Defaults to ``1970``.

``DJCOPYRIGHT_FORMAT_STRING``
    Contains format string to show copyright. Defaults to ``"{start_year} - {current_year}"``.

``DJCOPYRIGHT_SHOW_CURRENT_YEAR``
    Show current year in copyright string. Defaults to ``True``.

``DJCOPYRIGHT_SHOW_START_YEAR``
    Show start year in copyright string. Defaults to ``True``.

Usage
-----
If you want always have ``"COPYRIGHT_YEARS"`` variable in templates context, just add ``"djcopyright.context_processors.djcopyright_years"`` to ``settings.TEMPLATE_CONTEXT_PROCESSORS``

.. code-block:: python

    # settings.py

    TEMPLATE_CONTEXT_PROCESSORS += [
        "djcopyright.context_processors.djcopyright_years",
    ]


Else you can use ``djcopyright_years`` templatetag which can be loaded from ``djcopyright_tags``.

.. code-block:: django

    {# footer.html #}

    {% load djcopyright_tags %}

    {% djcopyright_years as COPYRIGHT_YEARS %}
    {{ COPYRIGHT_YEARS }}

Licensing
---------
django-djcopyright is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.
For complete license text see COPYING file.

Contacts
--------
**Project Website**: https://github.com/vint21h/django-djcopyright/

**Author**: Alexei Andrushievich <vint21h@vint21h.pp.ua>

For other authors list see AUTHORS file.


.. |Travis| image:: https://travis-ci.com/vint21h/django-djcopyright.svg?branch=master
    :alt: Travis
.. |Coveralls| image:: https://coveralls.io/repos/github/vint21h/django-djcopyright/badge.svg?branch=master
    :alt: Coveralls
.. |Requires| image:: https://requires.io/github/vint21h/django-djcopyright/requirements.svg?branch=master
    :alt: Requires
.. |pypi-license| image:: https://img.shields.io/pypi/l/django-djcopyright
    :alt: License
.. |pypi-version| image:: https://img.shields.io/pypi/v/django-djcopyright
    :alt: Version
.. |pypi-django-version| image:: https://img.shields.io/pypi/djversions/django-djcopyright
    :alt: Supported Django version
.. |pypi-python-version| image:: https://img.shields.io/pypi/pyversions/django-djcopyright
    :alt: Supported Python version
.. |pypi-format| image:: https://img.shields.io/pypi/format/django-djcopyright
    :alt: Package format
.. |pypi-wheel| image:: https://img.shields.io/pypi/wheel/django-djcopyright
    :alt: Python wheel support
.. |pypi-status| image:: https://img.shields.io/pypi/status/django-djcopyright
    :alt: Package status
.. _Travis: https://travis-ci.com/vint21h/django-djcopyright/
.. _Coveralls: https://coveralls.io/github/vint21h/django-djcopyright?branch=master
.. _Requires: https://requires.io/github/vint21h/django-djcopyright/requirements/?branch=master
.. _pypi-license: https://pypi.org/project/django-djcopyright/
.. _pypi-version: https://pypi.org/project/django-djcopyright/
.. _pypi-django-version: https://pypi.org/project/django-djcopyright/
.. _pypi-python-version: https://pypi.org/project/django-djcopyright/
.. _pypi-format: https://pypi.org/project/django-djcopyright/
.. _pypi-wheel: https://pypi.org/project/django-djcopyright/
.. _pypi-status: https://pypi.org/project/django-djcopyright/

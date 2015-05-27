.. django-djcopyright
.. README.rst

A django-djcopyright documentation
==================================

    *django-djcopyright is a django reusable application to show pretty formatted copyright years*

.. contents::

Installation
------------
* Obtain your copy of source code from git repository: ``git clone https://github.com/vint21h/django-djcopyright.git``. Or download latest release from https://github.com/vint21h/django-djcopyright/tags.
* Run ``python ./setup.py install`` from repository source tree or unpacked archive. Or use pip: ``pip install django-djcopyright``.

Configuration
-------------
Add ``"djcopyright"`` to ``settings.INSTALLED_APPS``.

    INSTALLED_APPS = (
        ...,

        "djcopyright",

        ...,

    )


Djcopyright settings
--------------------
``DJCOPYRIGHT_START_YEAR``
    Contains year to start show copyright from. Defaults to ``1970``.

``DJCOPYRIGHT_FORMAT_STRING``
    Contains format string to show copyright. Defaults to ``u"{start_year} - {current_year}"``.

``DJCOPYRIGHT_SHOW_CURRENT_YEAR``
    Show current year in copyright string. Defaults to ``True``.

``DJCOPYRIGHT_SHOW_START_YEAR``
    Show start year in copyright string. Defaults to ``True``.

Usage
-----
If you want always have ``COPYRIGHT_YEARS`` variable in templates context, just add ``"djcopyright.context_processors.djcopyright_years"`` to ``settings.TEMPLATE_CONTEXT_PROCESSORS``

    TEMPLATE_CONTEXT_PROCESSORS = (
        ...,

        "djcopyright.context_processors.djcopyright_years",

        ...,

    )


Else you can use ``djcopyright_years`` assignment templatetag which can be loaded from ``djcopyright_tags``.

Licensing
---------
django-djcopyright is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.
For complete license text see COPYING file.

Contacts
--------
**Project Website**: https://github.com/vint21h/django-djcopyright

**Author**: Alexei Andrushievich <vint21h@vint21h.pp.ua>

For other authors list see AUTHORS file.

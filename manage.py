#!/usr/bin/env python

# -*- coding: utf-8 -*-

# django-djcopyright
# manage.py


import os
import sys


if __name__ == "__main__":

    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "tests.settings")

    try:
        from django.core.management import execute_from_command_line
    except ImportError:
        try:
            import django  # noqa: F401, pylint: disable=W0611
        except ImportError:
            raise ImportError(
                "Couldn't import Django. Are you sure it's installed and "
                "available on your PYTHONPATH environment variable? Did you "
                "forget to activate a virtual environment?"
            )
        raise

    execute_from_command_line(sys.argv)

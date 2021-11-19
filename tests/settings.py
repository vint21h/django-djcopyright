# -*- coding: utf-8 -*-

# django-djcopyright
# tests/settings.py


import sys
import pathlib
import datetime
from random import SystemRandom
from typing import Dict, List, Union


# black magic to use imports from library code
path = pathlib.Path(__file__).absolute()
project = path.parent.parent.parent
sys.path.insert(0, str(project))


# secret key
SECRET_KEY: str = "".join(
    [
        SystemRandom().choice("abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*(-_=+)")
        for i in range(50)
    ]
)

# configure databases
DATABASES: Dict[str, Dict[str, str]] = {
    "default": {"ENGINE": "django.db.backends.sqlite3", "NAME": ":memory:"}
}

# configure templates
TEMPLATES: List[Dict[str, Union[str, List[str], bool, Dict[str, str]]]] = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {},
    }
]


INSTALLED_APPS: List[str] = ["djcopyright"]

# configure urls
ROOT_URLCONF: str = "djcopyright.urls"

# django copyright settings
DJCOPYRIGHT_START_YEAR: int = datetime.date.today().year
DJCOPYRIGHT_SHOW_CURRENT_YEAR: bool = True
DJCOPYRIGHT_SHOW_START_YEAR: int = True
DJCOPYRIGHT_FORMAT_STRING: str = "{start_year} - {current_year}"  # noqa: FS003

#!/usr/bin/env python
# -*- coding: utf-8 -*-

# django-djcopyright
# setup.py

from setuptools import setup, find_packages

# metadata
VERSION = (0, 2, 3)
__version__ = ".".join(map(str, VERSION))

setup(
    name="django-djcopyright",
    version=__version__,
    packages=find_packages(),
    install_requires=["Django", ],
    author="Alexei Andrushievich",
    author_email="vint21h@vint21h.pp.ua",
    description="Django reusable app to show pretty formatted copyright years",
    license="GPLv3 or later",
    url="https://github.com/vint21h/django-djcopyright",
    download_url="https://github.com/vint21h/django-djcopyright/archive/{version}.tar.gz".format(version= __version__),
    zip_safe=False,
    include_package_data=True,
    classifiers=[
        "Environment :: Plugins",
        "License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)",
        "Operating System :: Unix",
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Topic :: Utilities",
        "Framework :: Django :: 1.5",
        "Framework :: Django :: 1.6",
        "Framework :: Django :: 1.7",
        "Framework :: Django :: 1.8",
    ]
)

# -*- coding: utf-8 -*-

"""Top-level package for {{ cookiecutter.python_slug }}."""

__author__ = "{{ cookiecutter.name }}"
__email__ = "{{ cookiecutter.email }}"
# Do not edit this string manually, always use bumpversion
# Details in CONTRIBUTING.md
__version__ = "0.0.0"


def get_module_version() -> str:
    return __version__

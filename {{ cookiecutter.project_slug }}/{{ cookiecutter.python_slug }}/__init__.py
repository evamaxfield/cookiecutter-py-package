# -*- coding: utf-8 -*-

"""Top-level package for {{ cookiecutter.python_slug }}."""

from importlib.metadata import PackageNotFoundError, version

try:
    __version__ = version("{{ cookiecutter.project_slug }}")
except PackageNotFoundError:
    __version__ = "uninstalled"

__author__ = "{{ cookiecutter.author_name }}"
__email__ = "{{ cookiecutter.author_email }}"


def get_module_version() -> str:
    return __version__

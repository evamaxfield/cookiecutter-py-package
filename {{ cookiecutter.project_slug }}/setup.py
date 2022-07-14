#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The setup script."""

from setuptools import find_packages, setup

with open("README.md") as readme_file:
    readme = readme_file.read()

setup_requirements = [
    "pytest-runner>=5.2",
]

docs_requirements = [
    "m2r2>=0.2.7",
    "Sphinx>=4.0.0",
    "furo>=2022.4.7",
    # Extensions
    "numpydoc",
    "sphinx-click",
    "sphinx-copybutton",
    "sphinx-remove-toctrees",
    "sphinx_autosummary_accessors",
    "sphinx-tabs",
    "sphinx-design",
]

ci_requirements = [
    "codecov>=2.1.4",
    "tox>=3.15.2",
]

test_requirements = [
    *ci_requirements,
    "black>=22.3.0",
    "flake8>=3.8.3",
    "flake8-debugger>=3.2.1",
    "isort>=5.7.0",
    "mypy>=0.790",
    "pytest>=5.4.3",
    "pytest-cov>=2.9.0",
    "pytest-raises>=0.11",
]

dev_requirements = [
    *setup_requirements,
    *test_requirements,
    *docs_requirements,
    "bump2version>=1.0.1",
    "coverage>=5.1",
    "twine>=3.1.1",
    "wheel>=0.34.2",
]

requirements = []

extra_requirements = {
    "setup": setup_requirements,
    "ci": ci_requirements,
    "test": test_requirements,
    "dev": dev_requirements,
    "all": [
        *requirements,
        *dev_requirements,
    ],
}

setup(
    author="{{ cookiecutter.name }}",
    author_email="{{ cookiecutter.email }}",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ],
    description="{{ cookiecutter.project_short_description }}",
    entry_points={
        "console_scripts": [
            ("calc-string-length={{ cookiecutter.python_slug }}.bin.str_len:main"),
        ],
    },
    install_requires=requirements,
    license="{{ cookiecutter.license }}",
    long_description=readme,
    long_description_content_type="text/markdown",
    include_package_data=True,
    name="{{ cookiecutter.project_slug }}",
    packages=find_packages(exclude=["tests", "*.tests", "*.tests.*"]),
    python_requires=">=3.8",
    setup_requires=setup_requirements,
    test_suite="{{ cookiecutter.python_slug }}/tests",
    tests_require=test_requirements,
    extras_require=extra_requirements,
    url="https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}",
    # Do not edit this string manually, always use bumpversion
    # Details in CONTRIBUTING.rst
    version="0.0.0",
    zip_safe=False,
)

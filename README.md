# Cookiecutter Py Package

[![Example Repo Status](https://github.com/evamaxfield/cookiecutter-py-package/workflows/Generate%20and%20Test%20Example%20Repo/badge.svg)](https://github.com/evamaxfield/cookiecutter-py-package/tree/example-build)

![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)

Yet another Cookiecutter template for a Python package.

## About

`Cookiecutter` is a Python package to generate templated projects.
This repository is a template for `cookiecutter` to generate a Python project which
contains following:

-   A directory structure for your project
-   Prebuilt `setup.py` file to help you develop and install your package
-   Includes basic examples of modules, tests, bin scripts, etc.
-   Continuous integration
    -   Preconfigured to generate project documentation
    -   Preconfigured to automatically run tests every time you push to GitHub
    -   Preconfigured to help you release your package publicly (PyPI)

We think that this template provides a good starting point for any Python project.

## Features

-   Uses `tox` (an environment manager) and `pytest` for local testing, simply run `tox`
    or `just build` from a terminal in the project home directory
-   Runs tests on Windows, Mac, and Ubuntu on every branch and pull request commit using
    GitHub Actions
-   Releases your Python Package to PyPI when you push to `main` after using
    `bump2version`
-   Automatically builds documentation using Sphinx on every push to main and deploys
    to GitHub Pages
-   Includes example code samples for objects, tests, and bin scripts

List of available `just` commands:
```bash
just
```
```
Available recipes:
    build                    # run tox / run tests and lint
    clean                    # clean all build, python, and lint files
    default                  # list all available commands
    generate-docs            # generate Sphinx HTML documentation
    lint                     # lint, format, and check all files
    serve-docs               # generate Sphinx HTML documentation and serve to browser
    update-from-cookiecutter # update this repo using latest cookiecutter-py-package
```

## Example

-   For an example of the base project that is built from this template, go to the
    [example-build branch](https://github.com/evamaxfield/cookiecutter-py-package/tree/example-build).

## Quickstart

To use this template use the following commands and then follow the prompts from the
terminal.

1. `pip install cookiecutter`
2. `cookiecutter gh:evamaxfield/cookiecutter-py-package`
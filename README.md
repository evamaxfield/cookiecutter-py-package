# Cookiecutter Py Package

[![Build Status](https://github.com/evamaxfield/cookiecutter-py-package/workflows/CI/badge.svg)](https://github.com/evamaxfield/cookiecutter-py-package/actions)

![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)

Yet another Cookiecutter template for a Python package.

## About

`Cookiecutter` is a Python package to generate templated projects.
This repository is a template for `cookiecutter` to generate a Python project which
contains following:

-   A directory structure for your project
-   Prebuilt `pyproject.toml` file to help you develop and install your package
-   Includes basic examples of modules, tests, bin scripts, etc.
-   Continuous integration
    -   Preconfigured to generate project documentation
    -   Preconfigured to automatically run tests every time you push to GitHub
    -   Preconfigured to help you release your package publicly (PyPI)

We think that this template provides a good starting point for any Python project.

## Quickstart

To use this template use the following commands.

1. `pip install cookiecutter`
2. `cookiecutter gh:evamaxfield/cookiecutter-py-package`

Once the project is generated, move to the newly created project directory
and follow the instructions in `SETUP.md`.

## Features

-   Uses `pytest` for local testing, simply run `just build` from a terminal.
-   Runs tests on Windows, Mac, and Ubuntu on every commit to `main` and
    every commit to branches with an open `pull request` to `main` using
    GitHub Actions.
-   Releases your Python Package to PyPI when you push to `main` after pushing a new
    git tag with `just tag-for-release` and `just release`.
-   Automatically builds documentation using Sphinx on every push to `main` and deploys
    to GitHub Pages.
-   Includes very minimal example code to get started.

List of available [just](https://github.com/casey/just) commands:
```bash
just
```
```
Available recipes:
    build                    # run lint and then run tests
    clean                    # clean all build, python, and lint files
    default                  # list all available commands
    generate-docs            # generate Sphinx HTML documentation
    install                  # install with all deps
    lint                     # lint, format, and check all files
    release                  # release a new version
    serve-docs               # generate Sphinx HTML documentation and serve to browser
    tag-for-release version  # tag a new version
    test                     # run tests
    update-from-cookiecutter # update this repo using latest cookiecutter-py-package
```
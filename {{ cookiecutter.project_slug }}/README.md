# {{ cookiecutter.project_slug }}

[![Build Status](https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}/workflows/Build/badge.svg)](https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}/actions)
[![Documentation](https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}/workflows/Documentation/badge.svg)](https://{{ cookiecutter.project_slug }}.github.io/{{ cookiecutter.project_slug }})

{{ cookiecutter.project_short_description }}

---

## Setting Up the Repo

1. Turn your project into a GitHub repository:
    - Make an account on [github.com](https://github.com)
    - Go to [make a new repository](https://github.com/new)
    - _Recommendations:_
        - _It is strongly recommended to make the repository name the same as the Python
            package name_
        - _A lot of the following optional steps are *free* if the repository is Public,
            plus open source is cool_
    - After a GitHub repo has been created, run the commands listed under:
        "...or push an existing repository from the command line"
2. Ensure that you have set GitHub pages to build the `gh-pages` branch by selecting the
   `gh-pages` branch in the dropdown in the "GitHub Pages" section of the
   repository settings.
   ([Repo Settings](https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}/settings))
3. Register your project with PyPI:
    - Make an account on [pypi.org](https://pypi.org)
    - Go to your GitHub repository's settings and under the
      [Secrets tab](https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}/settings/secrets/actions),
      add a secret called `PYPI_TOKEN` with your password for your PyPI account.
      Don't worry, no one will see this password because it will be encrypted.
    - Next time you push to the branch `main` after using `bump2version`, GitHub
      actions will build and deploy your Python package to PyPI.

You can delete this entire "Setting up the Repo" section once done!

## Installation

**Stable Release:** `pip install {{ cookiecutter.project_slug }}`<br>
**Development Head:** `pip install git+https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}.git`

## Quickstart

```python
from {{ cookiecutter.python_slug }} import example

print(example.str_len("hello"))  # prints 5
```

## Documentation

For full package documentation please visit [{{ cookiecutter.github_username }}.github.io/{{ cookiecutter.project_slug }}](https://{{ cookiecutter.github_username }}.github.io/{{ cookiecutter.project_slug }}).

## Development

See [CONTRIBUTING.md](CONTRIBUTING.md) for information related to developing the code.

For development commands we use [just](https://github.com/casey/just).

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

**{{ cookiecutter.license }}**

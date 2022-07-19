# {{ cookiecutter.project_slug }}

[![Build Status](https://github.com/{{ cookiecutter.hosting_github_username_or_org }}/{{ cookiecutter.project_slug }}/workflows/Build/badge.svg)](https://github.com/{{ cookiecutter.hosting_github_username_or_org }}/{{ cookiecutter.project_slug }}/actions)
[![Documentation](https://github.com/{{ cookiecutter.hosting_github_username_or_org }}/{{ cookiecutter.project_slug }}/workflows/Documentation/badge.svg)](https://{{ cookiecutter.hosting_github_username_or_org }}.github.io/{{ cookiecutter.project_slug }})

{{ cookiecutter.project_short_description }}

---

## Installation

**Stable Release:** `pip install {{ cookiecutter.project_slug }}`<br>
**Development Head:** `pip install git+https://github.com/{{ cookiecutter.hosting_github_username_or_org }}/{{ cookiecutter.project_slug }}.git`

## Quickstart

```python
from {{ cookiecutter.python_slug }} import example

print(example.str_len("hello"))  # prints 5
```

## Documentation

For full package documentation please visit [{{ cookiecutter.hosting_github_username_or_org }}.github.io/{{ cookiecutter.project_slug }}](https://{{ cookiecutter.hosting_github_username_or_org }}.github.io/{{ cookiecutter.project_slug }}).

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

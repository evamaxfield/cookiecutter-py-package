# python-boilerplate

[![Build Status](https://github.com/JaneCodes/python-boilerplate/workflows/Build/badge.svg)](https://github.com/JaneCodes/python-boilerplate/actions)
[![Documentation](https://github.com/JaneCodes/python-boilerplate/workflows/Documentation/badge.svg)](https://JaneCodes.github.io/python-boilerplate)

Python Boilerplate contains all the boilerplate you need to create a Python package.

---

## Installation

**Stable Release:** `pip install python-boilerplate`<br>
**Development Head:** `pip install git+https://github.com/JaneCodes/python-boilerplate.git`

## Quickstart

```python
from python_boilerplate import example

print(example.str_len("hello"))  # prints 5
```

## Documentation

For full package documentation please visit [JaneCodes.github.io/python-boilerplate](https://JaneCodes.github.io/python-boilerplate).

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

**MIT License**

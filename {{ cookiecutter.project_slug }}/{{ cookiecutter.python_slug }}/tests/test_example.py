#!/usr/bin/env python

import pytest

from {{ cookiecutter.python_slug }} import example


@pytest.mark.parametrize(
    "string, count",
    [
        ("string", 6),
        ("hello", 5),
        ("world", 5),
        ("defenestration", 14),
    ],
)
def test_str_len(string: str, count: int) -> None:
    assert example.str_len(string) == count

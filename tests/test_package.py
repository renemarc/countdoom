#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `countdoom` package."""

import subprocess

import countdoom


def test_package_main() -> None:
    """
    Test package usage.

    This check uses a subprocess to validate the package, since the
    package's __main__.py cannot be imported for tests.
    """
    process = subprocess.Popen(
        ['python', '-m', 'countdoom', '--version'],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )
    stdout = process.communicate()[0]

    assert 'countdoom {}'.format(countdoom.__version__) in str(stdout)

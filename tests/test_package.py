#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `doomsday_clock` package."""

import subprocess

import doomsday_clock


def test_package_main() -> None:
    """
    Test package usage.

    This check uses a subprocess to validate the package, since the
    package's __main__.py cannot be imported for tests.
    """
    process = subprocess.Popen(
        ['python', '-m', 'doomsday_clock', '--version'],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )
    stdout = process.communicate()[0]

    assert 'doomsday_clock {}'.format(doomsday_clock.__version__) in str(
        stdout
    )

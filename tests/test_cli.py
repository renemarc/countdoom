#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Tests for `command-line interface` module.
"""

import pytest

from doomsday_clock import cli


def test_cli_help(capfd) -> None:
    """Test the CLI."""

    cli.main(['-h'])
    out, err = capfd.readouterr()
    assert '-h, --help            show this help message and exit' in out

    cli.main(['--help'])
    out, err = capfd.readouterr()
    assert '-h, --help            show this help message and exit' in out


def test_cli_version(capfd) -> None:
    """Test the CLI."""
    with pytest.raises(SystemExit) as exception:
        cli.main(['--version'])

    assert exception.type == SystemExit
    # assert exception.value == 'doomsday_py 0.1.0'
    assert exception.value.code == 0


def test_cli_parser_help() -> None:
    """Test the CLI."""

    parser = cli.create_parser()
    args = cli.parse_args(parser, ['--help'])
    assert args.help is True


def test_cli_parser_dummy() -> None:
    """Test the CLI."""

    parser = cli.create_parser()
    with pytest.raises(SystemExit) as err:
        cli.parse_args(parser, ['--dummy'])

    assert err.type == SystemExit
    assert err.value.code == 2

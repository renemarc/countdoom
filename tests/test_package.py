#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Tests for `doomsday_clock` package.
"""

# import argparse
# from argparse import ArgumentError
# from unittest import mock
#
# import pytest
#
# import doomsday_clock
# from doomsday_clock import cli

# from doomsday_clock import parse_args


#
# def test_package_main(capfd) -> None:
#     """Test the CLI."""
#
#     import doomsday_clock as module
#     with mock.patch.object(module, "main", return_value=42):
#         with mock.patch.object(module, "__name__", "__main__"):
#             with mock.patch.object(module.sys, 'exit') as mock_exit:
#                 module.main()
#
#                 assert mock_exit.call_args[0][0] == 42

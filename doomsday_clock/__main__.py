# -*- coding: utf-8 -*-

"""
Top-level script environment for Doomsday Clock.
"""

import sys

import cli


def main():
    sys.exit(cli.main(sys.argv[1:]))


main()

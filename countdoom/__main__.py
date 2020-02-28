# -*- coding: utf-8 -*-

"""Top-level module for Countdoom."""
import os
import sys


def main() -> None:  # pragma: no cover
    """Run Countdoom client when package is called directly."""
    sys.path.append(os.getcwd())

    from countdoom import cli  # pylint: disable=C0415

    cli.cli()


main()  # pragma: no cover

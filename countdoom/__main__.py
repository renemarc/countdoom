# -*- coding: utf-8 -*-

"""Top-level module for Countdoom."""
import asyncio
import os
import sys


def main() -> None:  # pragma: no cover
    """Run Countdoom client when package is called directly."""
    sys.path.append(os.getcwd())
    from countdoom import cli  # pylint: disable=C0415

    loop = asyncio.get_event_loop()
    try:
        loop.run_until_complete(cli.main(sys.argv[1:]))
    finally:
        loop.close()


main()  # pragma: no cover

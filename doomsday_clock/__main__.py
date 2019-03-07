# -*- coding: utf-8 -*-

"""Top-level module for Doomsday Clock."""


def main() -> None:  # pragma: no cover
    """Run Doomsday Clock client when package is called directly."""
    import sys
    import asyncio
    import os

    sys.path.append(os.getcwd())
    from doomsday_clock import cli

    loop = asyncio.get_event_loop()
    try:
        loop.run_until_complete(cli.main(sys.argv[1:]))
    finally:
        loop.close()


main()  # pragma: no cover

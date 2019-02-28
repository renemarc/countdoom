# -*- coding: utf-8 -*-

"""
Console script for doomsday_clock.
"""
import argparse
import asyncio
import json
import sys
from argparse import ArgumentParser, Namespace

from doomsday_clock import DoomsdayClock, DoomsdayClockError

basic_formats = ('sentence', 'clock', 'time', 'countdown')


def main(args=None):
    """
    Console script for doomsday_clock.
    """
    header = "\n"
    header += " 11 12   ️\n"
    header += "10 \\|     Doomsday Py v0.1.0 🤯 🌊 ☢️  ☠ \n"
    header += "9   @     World threat assessment from TheBulletin.org\n"

    # Handle command-line interface
    parser = create_parser()
    args = parse_args(parser, args)

    # Print the overridden help
    if args.help:
        print(header)
        parser.print_help()
        return

    # Get current Doomsday Clock value
    client = DoomsdayClock(timeout=args.timeout)
    loop = asyncio.get_event_loop()
    task = loop.create_task(client.fetch_data())
    try:
        data = loop.run_until_complete(task)
    except DoomsdayClockError as err:
        print(err)
        return

    # Output results
    if args.format in basic_formats:
        print(data[args.format])
    elif args.format == 'json':
        print(json.dumps(data, indent=4))
    else:
        if data['countdown'].is_integer():
            data['countdown'] = int(data['countdown'])
        print(header)
        print("Sentence: {}".format(data['sentence']))
        print("Clock: {}".format(data['clock']))
        print("Time: {}".format(data['time']))
        print(
            "Countdown: {} minute{}".format(
                data['countdown'], 's' if data['countdown'] != 1 else ''
            )
        )
        print('')
    return header


def create_parser() -> ArgumentParser:
    """
    Factory function to create an argument parser.

    :return: Argument parser
    """

    def check_positive(value):
        """Allow only positive, non-zero integers"""
        int_value = int(value)
        if int_value <= 0:
            raise argparse.ArgumentTypeError(
                "{} is an invalid positive integer value".format(value)
            )
        return int_value

    parser = argparse.ArgumentParser(
        prog='doomsday_py',
        add_help=False,
        epilog="Be the change you want to see in the world.",
    )
    parser.add_argument(
        '--format',
        required=False,
        choices=basic_formats + ('all', 'json'),
        default='all',
        help="return data format (default: %(default)s).",
    )
    parser.add_argument(
        '--timeout',
        required=False,
        type=check_positive,
        default=DoomsdayClock.REQUEST_TIMEOUT,
        help="connection/request timeout in seconds (default: %(default)s).",
    )
    parser.add_argument(
        '--v', '--version', action='version', version='%(prog)s 0.1.0'
    )
    parser.add_argument(
        '-h',
        '--help',
        action="store_true",
        help="show this help message and exit",
    )
    return parser


def parse_args(parser: ArgumentParser, args: list) -> Namespace:
    return parser.parse_args(args)


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover

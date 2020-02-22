# -*- coding: utf-8 -*-

"""Console script for Countdoom."""
import argparse
import asyncio
import json
import sys
from argparse import ArgumentParser, Namespace

import countdoom

from .client import CountdoomClient, CountdoomClientError

BASIC_FORMATS = ('sentence', 'clock', 'time', 'minutes', 'countdown')

HEADER = """
 11 12   ️
10 \\|     Countdoom: Doomsday Clock 🤯 🌊 ☢️  ☠️
9   @     World threat assessment from TheBulletin.org
"""

MINUTE_FRACTIONS = (0, 30)


async def main(args=None):
    """Console script for countdoom."""
    # Handle command-line interface
    parser = create_parser()
    args = parse_args(parser, args)

    # Print the overridden help
    if args.help:
        print_header()
        parser.print_help()
        return

    # Get current Doomsday Clock value
    countdoom_client = CountdoomClient(timeout=args.timeout)
    try:
        data = await countdoom_client.fetch_data()
    except CountdoomClientError as err:
        print(err, file=sys.stderr)
        sys.exit(1)
    # loop = asyncio.get_event_loop()
    # task = loop.create_task(countdoom_client.fetch_data())
    # try:
    #     data = loop.run_until_complete(task)
    # except CountdoomClientError as err:
    #     print(err)
    #     return

    print_results(data, args)

    return


def create_parser() -> ArgumentParser:
    """
    Create an argument parser.

    :return: Argument parser
    """
    parser = argparse.ArgumentParser(
        prog='countdoom',
        add_help=False,
        epilog='"Be the change you want to see in the world." \
            —Gandhi/Arleen Lorrance',
    )

    def check_positive(value) -> int:
        """
        Allow only positive, non-zero integers.

        :param value: Integer as a string

        :return: An actual integer

        :raise ArgumentTypeError: If number is not positive
        """
        int_value = int(value)
        if int_value <= 0:
            raise argparse.ArgumentTypeError(
                "{} is an invalid positive integer value".format(value)
            )
        return int_value

    parser.add_argument(
        '--format',
        required=False,
        choices=BASIC_FORMATS + ('all', 'json'),
        default='all',
        help="return data format (default: %(default)s).",
    )
    parser.add_argument(
        '--timeout',
        required=False,
        type=check_positive,
        default=CountdoomClient.REQUEST_TIMEOUT,
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
    """
    Feed a list of arguments into ArgumentParser for processing.

    :param parser: ArgumentParser instance
    :param args: list of arguments

    :return: ArgumentParser Namespace object
    """
    return parser.parse_args(args)


def print_header() -> None:
    """Display a stylized header."""
    print(HEADER.format(countdoom.__version__))


def print_results(data: dict, args: Namespace) -> None:
    """
    Display command results in a variety of formats.

    :param data: command results
    :param args: ArgumentParser Namespace object
    """
    if args.format in BASIC_FORMATS:
        print(data[args.format])
    elif args.format == 'json':
        print(json.dumps(data, indent=4))
    else:
        unit = 'second'
        if (
            data['countdown'] >= 60
            and data['countdown'] % 60 in MINUTE_FRACTIONS
        ):
            data['countdown'] = round(data['countdown'] / 60, 2)
            unit = 'minute'
        if data['countdown'].is_integer():
            data['countdown'] = int(data['countdown'])
        print_header()
        print("Sentence: {}".format(data['sentence']))
        print("Clock: {}".format(data['clock']))
        print("Time: {}".format(data['time']))
        print("Minutes: {}".format(data['minutes']))
        print("Seconds: {}".format(data['countdown']))
        print(
            "Countdown: {} {}{}".format(
                data['countdown'], unit, 's' if data['countdown'] != 1 else ''
            )
        )
        print('')


if __name__ == "__main__":  # pragma: no cover
    LOOP = asyncio.get_event_loop()
    try:
        LOOP.run_until_complete(main())
    finally:
        LOOP.close()
    sys.exit()
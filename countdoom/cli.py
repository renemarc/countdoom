# -*- coding: utf-8 -*-

"""Console script for Countdoom."""

import argparse
import asyncio
import json
import sys
from argparse import ArgumentParser, Namespace
from typing import Any, Dict, List, Optional

import countdoom

from .client import CountdoomClient, CountdoomClientError

BASIC_FORMATS = ('sentence', 'clock', 'time', 'minutes', 'countdown')

HEADER = """
 11 12   ️
10 \\|      Countdoom: Doomsday Clock 🤯 🌊 ☢️  ☠️
9   @      World threat assessment from TheBulletin.org
"""

MINUTE_FRACTIONS = (0, 30)


def cli(args: Optional[List[Any]] = None) -> None:  # pragma: no cover
    """
    Run Countdoom client.

    :param args: list of arguments
    """
    if args is None:
        args = sys.argv[1:]
    loop = asyncio.get_event_loop()
    try:
        loop.run_until_complete(main(args))
    finally:
        loop.close()


async def main(args: Optional[List[Any]] = None) -> None:
    """
    Console script for Countdoom.

    :param args: list of arguments

    :raise CountdoomClientError: If an error is generated while fetching data
    """
    if args is None:
        args = []

    # Handle command-line interface
    parser = create_parser()
    parsed = vars(parse_args(parser, args))

    # Print the overridden help
    if parsed.get('help'):
        print_header()
        parser.print_help()
        return

    # Get current Doomsday Clock value
    params = {}  # type: Dict[str, Any]
    if 'timeout' in parsed:
        params['timeout'] = parsed.get('timeout')
    countdoom_client = CountdoomClient(**params)
    try:
        data = await countdoom_client.fetch_data()
    except CountdoomClientError as err:
        print(err, file=sys.stderr)
        sys.exit(1)

    print_results(data, parsed)
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
        '--v',
        '--version',
        action='version',
        version='%(prog)s {version}'.format(version=countdoom.__version__),
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


def print_results(data: dict, args: Dict[str, Any]) -> None:
    """
    Display command results in a variety of formats.

    :param data: command results
    :param args: ArgumentParser Namespace object
    """
    scheme = args.get('format')

    if scheme in BASIC_FORMATS:
        print(data[scheme])
        return

    if scheme == 'json':
        print(json.dumps(data, indent=4))
        return

    data['seconds'] = data['countdown']
    unit = 'second'

    if data['countdown'] >= 60 and data['countdown'] % 60 in MINUTE_FRACTIONS:
        data['countdown'] = round(data['countdown'] / 60, 2)
        unit = 'minute'

    if data['countdown'].is_integer():
        data['countdown'] = int(data['countdown'])

    if data['seconds'].is_integer():
        data['seconds'] = int(data['seconds'])

    seperator = "\n"
    segments = (
        ' Sentence: {sentence}',
        '    Clock: {clock}',
        '     Time: {time}',
        '  Minutes: {minutes}',
        '  Seconds: {countdown}',
        'Countdown: {countdown} {unit}{plural}',
    )
    output = seperator.join(segments)
    output = output.format(
        sentence=data['sentence'],
        clock=data['clock'],
        time=data['time'],
        minutes=data['minutes'],
        seconds=data['seconds'],
        countdown=data['countdown'],
        unit=unit,
        plural='s' if data['countdown'] != 1 else '',
    )
    print_header()
    print(output)

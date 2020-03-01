#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `command-line interface` module."""

import json

import pytest
from _pytest.capture import CaptureFixture
from aioresponses import aioresponses

import countdoom
from countdoom import CountdoomClient, cli


def _setup_mock_server(mocked: aioresponses) -> None:
    """
    Create internal server to mock website responses.

    :param mocked: aiohttp response
    """
    prefix = '<h3 class="{}">'.format(CountdoomClient.SELECTOR[1:])
    suffix = '</h3>'
    string = "IT IS 1 MINUTE TO MIDNIGHT"
    mocked.get(
        CountdoomClient.CLOCK_URL, status=200, body=prefix + string + suffix
    )


def test_cli_parser_help() -> None:
    """Test the CLI parser for `help` argument."""
    parser = cli.create_parser()
    args = cli.parse_args(parser, ['--help'])

    assert args.help is True


def test_cli_parser_timeout() -> None:
    """Test the CLI parser for `timeout` argument."""
    timeout = CountdoomClient.REQUEST_TIMEOUT - 1
    parser = cli.create_parser()
    args = cli.parse_args(parser, ['--timeout', str(timeout)])

    assert 'timeout' in args
    assert args.timeout == 9


def test_cli_parser_timeout_default() -> None:
    """Test the CLI parser for `timeout` argument's default value."""
    parser = cli.create_parser()
    args = cli.parse_args(parser, [])

    assert 'timeout' in args
    assert args.timeout == CountdoomClient.REQUEST_TIMEOUT


def test_cli_parser_timeout_non_positive(capsys: CaptureFixture) -> None:
    """
    Test the CLI parser's response when handing non-positive `timeout` values.

    :param capsys: System-level capture fixture
    """
    parser = cli.create_parser()
    with pytest.raises(SystemExit) as exception:
        cli.parse_args(parser, ['--timeout', 0])
    output = capsys.readouterr()

    assert exception.type == SystemExit
    assert exception.value.code == 2
    assert "0 is an invalid positive integer value" in output[1]


def test_cli_parser_unrecognized(capsys: CaptureFixture) -> None:
    """
    Test the CLI parser for unrecognized argument.

    :param capsys: System-level capture fixture
    """
    parser = cli.create_parser()
    with pytest.raises(SystemExit) as exception:
        cli.parse_args(parser, ['--dummy'])
    output = capsys.readouterr()

    assert exception.type == SystemExit
    assert exception.value.code == 2
    assert "unrecognized arguments: --dummy" in output[1]


@pytest.mark.asyncio
async def test_cli_request_help(capfd: CaptureFixture) -> None:
    """
    Test the CLI output for `help` argument.

    :param capfd: FileDescriptor-level capture fixture
    """
    await cli.main(['-h'])
    output = capfd.readouterr()
    assert '-h, --help            show this help message and exit' in output[0]

    await cli.main(['--help'])
    output = capfd.readouterr()
    assert '-h, --help            show this help message and exit' in output[0]


@pytest.mark.asyncio
async def test_cli_request_version(capsys: CaptureFixture) -> None:
    """
    Test the CLI output for `version` argument.

    :param capsys: System-level capture fixture
    """
    with pytest.raises(SystemExit) as exception:
        await cli.main(['--version'])
    output = capsys.readouterr()

    assert exception.type == SystemExit
    assert exception.value.code == 0
    assert "countdoom {}".format(countdoom.__version__) in output[0]


@pytest.mark.asyncio
async def test_cli_request_sentence(capsys: CaptureFixture) -> None:
    """
    Test the CLI output for `sentence` format.

    :param capsys: System-level capture fixture
    """
    with aioresponses() as mocked:
        _setup_mock_server(mocked)
        await cli.main(['--format', 'sentence'])
        output = capsys.readouterr()

        assert "IT IS 1 MINUTE TO MIDNIGHT" in output[0]


@pytest.mark.asyncio
async def test_cli_request_clock(capsys: CaptureFixture) -> None:
    """
    Test the CLI output for `clock` format.

    :param capsys: System-level capture fixture
    """
    with aioresponses() as mocked:
        _setup_mock_server(mocked)
        await cli.main(['--format', 'clock'])
        output = capsys.readouterr()

        assert '11:59' in output[0]


@pytest.mark.asyncio
async def test_cli_request_time(capsys: CaptureFixture) -> None:
    """
    Test the CLI output for `time` format.

    :param capsys: System-level capture fixture
    """
    with aioresponses() as mocked:
        _setup_mock_server(mocked)
        await cli.main(['--format', 'time'])
        output = capsys.readouterr()

        assert '23:59:00' in output[0]


@pytest.mark.asyncio
async def test_cli_request_minutes(capsys: CaptureFixture) -> None:
    """
    Test the CLI output for `minutes` format.

    :param capsys: System-level capture fixture
    """
    with aioresponses() as mocked:
        _setup_mock_server(mocked)
        await cli.main(['--format', 'minutes'])
        output = capsys.readouterr()

        assert '1' in output[0]


@pytest.mark.asyncio
async def test_cli_request_countdown(capsys: CaptureFixture) -> None:
    """
    Test the CLI output for `countdown` format.

    :param capsys: System-level capture fixture
    """
    with aioresponses() as mocked:
        _setup_mock_server(mocked)
        await cli.main(['--format', 'countdown'])
        output = capsys.readouterr()

        assert '60.0' in output[0]


@pytest.mark.asyncio
async def test_cli_request_json(capsys: CaptureFixture) -> None:
    """
    Test the CLI output for `json` format.

    :param capsys: System-level capture fixture
    """
    with aioresponses() as mocked:
        _setup_mock_server(mocked)
        await cli.main(['--format', 'json'])
        output = capsys.readouterr()
        json_data = json.loads(output[0])

        assert 'sentence' in json_data
        assert 'clock' in json_data
        assert 'time' in json_data
        assert 'minutes' in json_data
        assert 'countdown' in json_data


@pytest.mark.asyncio
async def test_cli_request_all(capsys: CaptureFixture) -> None:
    """
    Test the CLI output for `all` (default) format.

    :param capsys: System-level capture fixture
    """
    with aioresponses() as mocked:
        _setup_mock_server(mocked)
        await cli.main(['--format', 'all'])
        output = capsys.readouterr()

        assert 'Sentence:' in output[0]
        assert 'Clock:' in output[0]
        assert 'Time:' in output[0]
        assert 'Minutes:' in output[0]
        assert 'Countdown:' in output[0]

        _setup_mock_server(mocked)
        await cli.main()
        output = capsys.readouterr()

        assert 'Sentence:' in output[0]
        assert 'Clock:' in output[0]
        assert 'Time:' in output[0]
        assert 'Minutes:' in output[0]
        assert 'Countdown:' in output[0]


@pytest.mark.asyncio
async def test_cli_request_unrecognized(capsys: CaptureFixture) -> None:
    """
    Test the CLI output for unrecognized argument.

    :param capsys: System-level capture fixture
    """
    with aioresponses() as mocked:
        _setup_mock_server(mocked)
        with pytest.raises(SystemExit) as exception:
            await cli.main(['--dummy'])
        output = capsys.readouterr()

        assert exception.value.code == 2
        assert 'unrecognized arguments' in output[1]


@pytest.mark.asyncio
async def test_cli_request_internal_error(capsys: CaptureFixture) -> None:
    """
    Test the CLI output when an internal error has occurred.

    :param capsys: System-level capture fixture
    """
    with aioresponses() as mocked:
        prefix = '<h3 class="{}">'.format(CountdoomClient.SELECTOR[1:])
        suffix = '</h3>'
        string = ' '
        mocked.get(
            CountdoomClient.CLOCK_URL,
            status=200,
            body=prefix + string + suffix,
        )
        with pytest.raises(SystemExit) as exception:
            await cli.main(['--format', 'clock'])
        output = capsys.readouterr()

        assert exception.value.code == 1
        assert 'Empty sentence found.' in output[1]

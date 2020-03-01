#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `client` module."""

import random
from typing import List, Optional, Tuple, Union

import pytest
import requests
from bs4 import BeautifulSoup
from pytest_httpserver import HTTPServer
from requests import Response

from countdoom.client import CountdoomClient, CountdoomClientError

SencenceList = List[
    Tuple[str, Optional[float], Optional[float], Optional[str], Optional[str]]
]
SENTENCES_VALID = [
    ("IT IS 16 MINUTES TO MIDNIGHT", 16, 16 * 60, '11:44', '23:44:00'),
    ("IT IS EIGHT MINUTES TO MIDNIGHT", 8, 8 * 60, '11:52', '23:52:00'),
    (
        "IT IS 3 AND A HALF MINUTES TO MIDNIGHT",
        3.5,
        3.5 * 60,
        '11:56:30',
        '23:56:30',
    ),
    ("IT IS STILL 4 MINUTES TO MIDNIGHT", 4, 4 * 60, '11:56', '23:56:00'),
    (
        "IT IS STILL 4 AND A HALF MINUTES TO MIDNIGHT",
        4.5,
        4.5 * 60,
        '11:55:30',
        '23:55:30',
    ),
    (
        "IT IS THREE AND A HALF MINUTES TO MIDNIGHT",
        3.5,
        3.5 * 60,
        '11:56:30',
        '23:56:30',
    ),
    (
        "IT IS STILL ONE AND A HALF MINUTES TO MIDNIGHT",
        1.5,
        1.5 * 60,
        '11:58:30',
        '23:58:30',
    ),
    ("IT IS 1 MINUTE TO MIDNIGHT", 1, 1 * 60, '11:59', '23:59:00'),
    ("IT IS ONE MINUTE TO MIDNIGHT", 1, 1 * 60, '11:59', '23:59:00'),
    (
        "IT IS 0 AND A HALF MINUTES TO MIDNIGHT",
        0.5,
        0.5 * 60,
        '11:59:30',
        '23:59:30',
    ),
    (
        "IT IS ZERO AND A HALF MINUTES TO MIDNIGHT",
        0.5,
        0.5 * 60,
        '11:59:30',
        '23:59:30',
    ),
    ("IT IS ZERO MINUTES TO MIDNIGHT", 0, 0, '12:00', '00:00:00'),
    ("IT IS 0 MINUTES TO MIDNIGHT", 0, 0, '12:00', '00:00:00'),
    ("IT IS 80 SECONDS TO MIDNIGHT", 1.33, 80, '11:58:40', '23:58:40'),
    ("IT IS STILL 80 SECONDS TO MIDNIGHT", 1.33, 80, '11:58:40', '23:58:40'),
    ("IT IS 60 SECONDS TO MIDNIGHT", 1, 60, '11:59', '23:59:00'),
    ("IT IS 30 SECONDS TO MIDNIGHT", 0.5, 30, '11:59:30', '23:59:30'),
    ("IT IS 1 SECOND TO MIDNIGHT", 0.02, 1, '11:59:59', '23:59:59'),
    ("IT IS STILL 1 SECOND TO MIDNIGHT", 0.02, 1, '11:59:59', '23:59:59'),
    (
        "IT IS 1 AND A HALF SECOND TO MIDNIGHT",
        0.03,
        1.5,
        '11:59:58',
        '23:59:58',
    ),
    (
        "IT IS STILL 1 AND A HALF SECOND TO MIDNIGHT",
        0.03,
        1.5,
        '11:59:58',
        '23:59:58',
    ),
    ("IT IS HALF A SECOND TO MIDNIGHT", 0.01, 0.5, '11:59:59', '23:59:59'),
    (
        "IT IS STILL HALF A SECOND TO MIDNIGHT",
        0.01,
        0.5,
        '11:59:59',
        '23:59:59',
    ),
    (
        "IT IS ZERO AND A HALF SECOND TO MIDNIGHT",
        0.01,
        0.5,
        '11:59:59',
        '23:59:59',
    ),
    ("IT IS ZERO SECONDS TO MIDNIGHT", 0, 0, '12:00', '00:00:00'),
    ("IT IS 0 SECONDS TO MIDNIGHT", 0, 0, '12:00', '00:00:00'),
]  # type: SencenceList
SENTENCES_INVALID = [
    ("IT IS DOOMSDAY MINUTES TO MIDNIGHT", None, None, None, None),
    ("APOCALYPSE YESTERDAY", None, None, None, None),
]  # type: SencenceList


@pytest.fixture(scope='module')
def response() -> Response:
    """
    Fetch a response from the source website.

    :return: Request response
    """
    return requests.get(CountdoomClient.CLOCK_URL)


def _get_path(string: str) -> str:
    """
    Create a path from a sentence.

    :param string: Slugged URL path

    :return: simple url-compatible path
    """
    return '-'.join(string.lower().split())


def _setup_servers(httpserver: HTTPServer) -> None:
    """
    Create local servers to mock website responses.

    :param httpserver: HTTP Server
    """
    prefix = '<h3 class="{}">'.format(CountdoomClient.SELECTOR[1:])
    suffix = '</h3>'

    sentences = SENTENCES_VALID + SENTENCES_INVALID
    # sentences = SENTENCES_VALID
    # for sentence in SENTENCES_INVALID:
    #     sentences.append(sentence)
    for sentence in sentences:
        path = _get_path(sentence[0])
        httpserver.expect_request('/{}'.format(path)).respond_with_data(
            prefix + sentence[0] + suffix
        )


@pytest.mark.live
def test_live_server_exists(response: Response) -> None:
    """
    Check if source server destination page has moved.

    :param response: Server response
    """
    assert (
        'Timeline'
        in BeautifulSoup(response.content, features="html.parser").title.string
    )


@pytest.mark.live
@pytest.mark.asyncio
async def test_live_server(response: Response) -> None:
    """
    Check if source server data format has changed.

    :param response: Server response
    """
    client = CountdoomClient()
    client.html = response.content.decode()
    data = await client.fetch_data()

    assert data is not None


@pytest.mark.asyncio
@pytest.mark.parametrize('sentence', [x[0] for x in SENTENCES_VALID])
async def test_valid_sentence(httpserver: HTTPServer, sentence: str) -> None:
    """
    Test parser for valid sentence extraction.

    :param httpserver: HTTP Server
    :param sentence: Doomsday Clock sentence
    """
    _setup_servers(httpserver)

    client = CountdoomClient()
    path = _get_path(sentence)
    client.CLOCK_URL = httpserver.url_for('/{}'.format(path))
    data = await client.fetch_data()

    assert data is not None
    assert sentence == data['sentence']


@pytest.mark.asyncio
@pytest.mark.parametrize(
    'sentence,countdown', [(x[0], x[2]) for x in SENTENCES_VALID]
)
async def test_valid_countdown(
    httpserver: HTTPServer, sentence: str, countdown: Union[int, float]
) -> None:
    """
    Test parser for countdown generation from valid sentences.

    :param httpserver: HTTP Server
    :param sentence: Doomsday Clock sentence
    :param countdown: Seconds to midnight
    """
    _setup_servers(httpserver)

    client = CountdoomClient()
    path = _get_path(sentence)
    client.CLOCK_URL = httpserver.url_for('/{}'.format(path))
    data = await client.fetch_data()

    assert data is not None
    assert countdown == data['countdown']


@pytest.mark.asyncio
@pytest.mark.parametrize(
    'sentence,minutes', [(x[0], x[1]) for x in SENTENCES_VALID]
)
async def test_valid_minutes(
    httpserver: HTTPServer, sentence: str, minutes: Union[int, float]
) -> None:
    """
    Test parser for countdown generation from valid sentences.

    :param httpserver: HTTP Server
    :param sentence: Doomsday Clock sentence
    :param minutes: Minutes to midnight
    """
    _setup_servers(httpserver)

    client = CountdoomClient()
    path = _get_path(sentence)
    client.CLOCK_URL = httpserver.url_for('/{}'.format(path))
    data = await client.fetch_data()

    assert data is not None
    assert minutes == data['minutes']


@pytest.mark.asyncio
@pytest.mark.parametrize(
    'sentence,clock', [(x[0], x[3]) for x in SENTENCES_VALID]
)
async def test_valid_clock(
    httpserver: HTTPServer, sentence: str, clock: str
) -> None:
    """
    Test parser for clock generation from valid sentences.

    :param httpserver: HTTP Server
    :param sentence: Doomsday Clock sentence
    :param clock: Clock representation of countdown to midnight
    """
    _setup_servers(httpserver)

    client = CountdoomClient()
    path = _get_path(sentence)
    client.CLOCK_URL = httpserver.url_for('/{}'.format(path))
    data = await client.fetch_data()

    assert data is not None
    assert clock == data['clock']
    assert clock == client.clock()


@pytest.mark.asyncio
@pytest.mark.parametrize(
    'sentence,time', [(x[0], x[4]) for x in SENTENCES_VALID]
)
async def test_valid_time(
    httpserver: HTTPServer, sentence: str, time: str
) -> None:
    """
    Test parser for time generation from valid sentences.

    :param httpserver: HTTP Server
    :param sentence: Doomsday Clock sentence
    :param time: Time representation of countdown to midnight
    """
    _setup_servers(httpserver)

    client = CountdoomClient()
    path = _get_path(sentence)
    client.CLOCK_URL = httpserver.url_for('/{}'.format(path))
    data = await client.fetch_data()

    assert data is not None
    assert time == data['time']
    assert time == client.time()


@pytest.mark.asyncio
@pytest.mark.parametrize(
    'sentence,minutes', [(x[0], x[1]) for x in SENTENCES_INVALID]
)
async def test_invalid_minutes(
    httpserver: HTTPServer, sentence: str, minutes: Union[int, float]
) -> None:
    """
    Test parser for minutes generation from invalid sentences.

    :param httpserver: HTTP Server
    :param sentence: Doomsday Clock sentence
    :param minutes: umber of minutes to midnight
    """
    _setup_servers(httpserver)

    client = CountdoomClient()
    path = _get_path(sentence)
    client.CLOCK_URL = httpserver.url_for('/{}'.format(path))
    with pytest.raises(CountdoomClientError) as err:
        await client.fetch_data()

    assert "Sentence not parsable." == str(err.value)
    assert minutes == client.minutes()


@pytest.mark.asyncio
@pytest.mark.parametrize(
    'sentence,clock', [(x[0], x[3]) for x in SENTENCES_INVALID]
)
async def test_invalid_clock(
    httpserver: HTTPServer, sentence: str, clock: str
) -> None:
    """
    Test parser for clock generation from invalid sentences.

    :param httpserver: HTTP Server
    :param sentence: Doomsday Clock sentence
    :param clock: Clock representation of countdown to midnight
    """
    _setup_servers(httpserver)

    client = CountdoomClient()
    path = _get_path(sentence)
    client.CLOCK_URL = httpserver.url_for('/{}'.format(path))
    with pytest.raises(CountdoomClientError) as err:
        await client.fetch_data()

    assert "Sentence not parsable." == str(err.value)
    assert clock == client.clock()


@pytest.mark.asyncio
@pytest.mark.parametrize(
    'sentence,time', [(x[0], x[4]) for x in SENTENCES_INVALID]
)
async def test_invalid_time(
    httpserver: HTTPServer, sentence: str, time: str
) -> None:
    """
    Test parser for time generation from invalid sentences.

    :param httpserver: HTTP Server
    :param sentence: Doomsday Clock sentence
    :param time: Time representation of countdown to midnight
    """
    _setup_servers(httpserver)

    client = CountdoomClient()
    path = _get_path(sentence)
    client.CLOCK_URL = httpserver.url_for('/{}'.format(path))
    with pytest.raises(CountdoomClientError) as err:
        await client.fetch_data()

    assert "Sentence not parsable." == str(err.value)
    assert time == client.time()


@pytest.mark.asyncio
async def test_invalid_selector(httpserver: HTTPServer) -> None:
    """
    Test for invalid HTML element selector.

    :param httpserver: HTTP Server
    """
    prefix = '<h3 class="{}">'.format(CountdoomClient.SELECTOR[1:])
    suffix = '</h3>'
    string = "IT IS 1 AND A HALF MINUTE TO MIDNIGHT"
    path = 'test_invalid_selector'
    httpserver.expect_request('/{}'.format(path)).respond_with_data(
        prefix + string + suffix
    )

    client = CountdoomClient()
    client.CLOCK_URL = httpserver.url_for('/{}'.format(path))
    client.SELECTOR = '.wrong-id-' + str(random.randint(0, 100000000))
    with pytest.raises(CountdoomClientError) as err:
        await client.fetch_data()

    assert "No sentence found." == str(err.value)


@pytest.mark.asyncio
async def test_htmlized_sentence(httpserver: HTTPServer) -> None:
    """
    Test for invalid HTML element selector.

    :param httpserver: HTTP Server
    """
    prefix = '<h3 class="{}">'.format(CountdoomClient.SELECTOR[1:])
    suffix = '</h3>'
    string = " IT  IS <em>STILL</em> 1 <b>MINUTE</b> TO  MIDNIGHT"
    path = 'test_htmlized_sentence'
    httpserver.expect_request('/{}'.format(path)).respond_with_data(
        prefix + string + suffix
    )

    client = CountdoomClient()
    client.CLOCK_URL = httpserver.url_for('/{}'.format(path))
    data = await client.fetch_data()

    assert data is not None
    assert '11:59' == data['clock']
    assert '11:59' == client.clock()


@pytest.mark.asyncio
async def test_empty_sentence(httpserver: HTTPServer) -> None:
    """
    Test for invalid HTML element selector.

    :param httpserver: HTTP Server
    """
    prefix = '<h3 class="{}">'.format(CountdoomClient.SELECTOR[1:])
    suffix = '</h3>'
    string = ' '
    path = 'test_empty_sentence'
    httpserver.expect_request('/{}'.format(path)).respond_with_data(
        prefix + string + suffix
    )

    client = CountdoomClient()
    client.CLOCK_URL = httpserver.url_for('/{}'.format(path))
    with pytest.raises(CountdoomClientError) as err:
        await client.fetch_data()

    assert "Empty sentence found." == str(err.value)


@pytest.mark.asyncio
async def test_null_sentence() -> None:
    """Test for sentence with None value."""
    client = CountdoomClient()
    with pytest.raises(CountdoomClientError) as err:
        client._sentence_to_countdown()  # pylint: disable=W0212

    assert "Sentence is null." == str(err.value)


def test_empty_clock() -> None:
    """Test clock result when sentence processing has not been performed."""
    client = CountdoomClient()
    clock = client.clock()

    assert clock is None


def test_empty_time() -> None:
    """Test time result when sentence processing has not been performed."""
    client = CountdoomClient()
    time = client.clock()

    assert time is None


@pytest.mark.asyncio
async def test_formatted_time(httpserver: HTTPServer) -> None:
    """
    Test for invalid HTML element selector.

    :param httpserver: HTTP Server
    """
    prefix = '<h3 class="{}">'.format(CountdoomClient.SELECTOR[1:])
    suffix = '</h3>'
    string = "IT IS 16 MINUTES TO MIDNIGHT"
    path = 'test_formatted_time'
    httpserver.expect_request('/{}'.format(path)).respond_with_data(
        prefix + string + suffix
    )

    client = CountdoomClient()
    client.CLOCK_URL = httpserver.url_for('/{}'.format(path))
    data = await client.fetch_data()

    assert '23:44:00' == data['time']
    assert '00:44:23' == client.time('%S:%M:%H')


@pytest.mark.asyncio
async def test_url_not_found(httpserver: HTTPServer) -> None:
    """
    Test fetching wrong URL.

    :param httpserver: HTTP Server
    """
    path = 'test_url_not_found'
    client = CountdoomClient()
    client.CLOCK_URL = httpserver.url_for('/{}'.format(path))
    with pytest.raises(CountdoomClientError) as err:
        await client.fetch_data()

    assert "Page not found." == str(err.value)


@pytest.mark.asyncio
async def test_server_not_found() -> None:
    """Test fetching wrong server."""
    client = CountdoomClient()
    client.CLOCK_URL = 'http://website.that-should.never-resolve'
    with pytest.raises(CountdoomClientError) as err:
        await client.fetch_data()

    assert "Cannot connect to website. Check URL." == str(err.value)


@pytest.mark.asyncio
async def test_session_not_started() -> None:
    """Test fetching without starting a session first."""
    client = CountdoomClient()
    with pytest.raises(CountdoomClientError) as err:
        await client._fetch(client.CLOCK_URL)  # pylint: disable=W0212

    assert "Session not started." == str(err.value)

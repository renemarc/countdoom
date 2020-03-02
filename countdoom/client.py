# -*- coding: utf-8 -*-

"""Client module."""

import datetime
import logging
import re
from typing import Dict, Optional, Union

import aiohttp
import async_timeout
from bs4 import BeautifulSoup

_LOGGER = logging.getLogger('countdoom')


class CountdoomClient:
    """
    Countdoom client.

    Convert Doomsday Clock data into parsable time from the Timeline page at
    https://thebulletin.org/doomsday-clock/past-announcements/

    Based on prior Node.js work by Matt Bierner.
    See https://github.com/mattbierner/MinutesToMidnight
    """

    CLOCK_URL = (
        'https://thebulletin.org/doomsday-clock/past-announcements/'
    )  # type: str
    SELECTOR = '.uabb-infobox-title'  # type: str
    REQUEST_TIMEOUT = 10  # type: int

    CLOCK_FORMAT_LONG = '%-I:%M:%S'  # type: str
    CLOCK_FORMAT_SHORT = '%-I:%M'  # type: str
    TIME_FORMAT = '%H:%M:%S'  # type: str

    def __init__(self, timeout: int = REQUEST_TIMEOUT) -> None:
        """
        Create a CountdoomClient object.

        :param timeout: Connection/request timeout
        """
        self.html = None  # type: Optional[str]
        self.timeout = timeout  # type: int
        self._countdown = None  # type: Optional[float]
        self._sentence = None  # type: Optional[str]
        self._session = None  # type: Optional[aiohttp.ClientSession]

    @property
    def countdown(self) -> Optional[float]:
        """
        Countdown to midnight.

        :return: Number of seconds to midnight
        """
        return self._countdown

    @property
    def sentence(self) -> Optional[str]:
        """
        Doomsday Clock sentence.

        :return: Doomsday Clock sentence
        """
        return self._sentence

    def clock(self) -> Optional[str]:
        """
        Convert countdown to midnight into a clock representation.

        :return: Clock representation of a countdown to midnight
        """
        if self._countdown is None:
            return None
        clock_format = (
            self.CLOCK_FORMAT_SHORT
            if self._countdown % 60 == 0
            else self.CLOCK_FORMAT_LONG
        )
        return self.countdown_to_time(self._countdown, clock_format)

    def minutes(self) -> Optional[float]:
        """
        Convert countdown to midnight into minutes to midnight representation.

        :return: Number of minutes to midnight
        """
        if self._countdown is None:
            return None
        minutes = float(self._countdown // 60)
        seconds = self._countdown % 60 / 60
        if seconds:
            minutes += round(seconds, 2)
        return minutes

    def time(self, time_format: str = TIME_FORMAT) -> Optional[str]:
        """
        Convert countdown to midnight into a time representation.

        :param time_format: ``strftime()`` time format

        :return: Time representation of a countdown to midnight
        """
        if self._countdown is None:
            return None
        return self.countdown_to_time(self._countdown, time_format)

    async def fetch_data(self) -> Dict[str, Union[str, float, None]]:
        """
        Retrieve the parsed Doomsday Clock.

        :return: Extracted sentence, clock, time, minutes, and countdown
        """
        try:
            if self.html is None:
                await self._get_session()
                await self._fetch_html()
            await self._extract_sentence()
        finally:
            await self.close()

        self._sentence_to_countdown()

        return {
            'sentence': self.sentence,
            'clock': self.clock(),
            'time': self.time(),
            'minutes': self.minutes(),
            'countdown': self.countdown,
        }

    async def _get_session(self) -> None:
        """Create an HTTP client session."""
        if self._session is None:
            self._session = aiohttp.ClientSession()

    async def _fetch_html(self) -> None:
        """Read the posted Doomsday Clock value."""
        self.html = await self._fetch(self.CLOCK_URL)

    async def _fetch(self, url: str, timeout: int = None) -> str:
        """
        Fetch a given web page.

        :param url: Link to a web page
        :param timeout: Connection/request timeout in seconds

        :return: Web page HTML body

        :raise CountdoomClientError: If session is not started
        :raise CountdoomClientError: If URL is not found
        :raise CountdoomClientError: If server connection fails
        """
        if self._session is None:
            raise CountdoomClientError("Session not started.")

        try:
            async with async_timeout.timeout(timeout):
                async with self._session.get(url, timeout=timeout) as resp:
                    if resp.status != 200:
                        raise AssertionError
                    return await resp.text()
        except AssertionError:
            await self.close()
            raise CountdoomClientError("Page not found.")
        except OSError:
            await self.close()
            raise CountdoomClientError("Cannot connect to website. Check URL.")

    async def _extract_sentence(self) -> None:
        """
        Read the posted Doomsday Clock value.

        :raise CountdoomClientError: If no sentence is found
        :raise CountdoomClientError: If empty sentence is found
        """
        html = BeautifulSoup(self.html, features='html.parser')

        # Find the first match, which is the current Doomsday Clock value.
        try:
            sentence = html.select(self.SELECTOR)[0].text
            self._sentence = re.sub(r'\s+', ' ', sentence).strip()
            if not self._sentence:
                raise ValueError()
        except IndexError:
            _LOGGER.error(
                "No sentence found using selector %s. Check for source "
                "website design changes.",
                self.SELECTOR,
            )
            raise CountdoomClientError("No sentence found.")
        except ValueError:
            _LOGGER.error(
                "Empty sentence found using selector %s. Check for source "
                "website design changes.",
                self.SELECTOR,
            )
            raise CountdoomClientError("Empty sentence found.")
        _LOGGER.debug("Sentence found: %s", self._sentence)

    async def close(self) -> None:
        """Close the HTTP connection."""
        if self._session is None:
            return
        if not self._session.closed:
            await self._session.close()
        self._session = None

    def _sentence_to_countdown(self) -> None:
        """
        Convert the Doomsday Clock sentence into a countdown to midnight.

        :raise CountdoomClientError: When sentence is null
        :raise CountdoomClientError: When sentence is not parsable
        """
        if self._sentence is None:
            raise CountdoomClientError("Sentence is null.")

        try:
            self._countdown = self.sentence_to_countdown(self._sentence)
        except AttributeError:
            _LOGGER.error(
                "Regex pattern yielded no result for : %s", self._sentence
            )
            raise CountdoomClientError("Sentence not parsable.")
        _LOGGER.debug("Countdown value: %s", self._countdown)

    @classmethod
    def sentence_to_countdown(cls, sentence: str) -> float:
        """
        Convert Doomsday Clock sentence to a number of seconds to midnight.

        :param sentence: Doomsday Clock sentence

        :return: A countdown to midnight

        :raise AttributeError: If sentence is not matched by regex pattern
        """
        pattern = (
            r"(?:(?P<integer>\d+)"
            r"|(?P<string>zero|one|two|three|four|five|six|seven|eight|nine)"
            r"|(?P<half>half))"
            r"(?P<and> and a half)?"
            r" (?P<unit>seconds|second|a second|minutes|minute|a minute)"
            r" to midnight"
        )
        result = re.search(pattern, sentence, re.M | re.I)

        if result is None:
            raise AttributeError

        countdown = 0.0
        # Integer unit.
        if result.group('integer'):
            countdown += int(result.group('integer'))
        # String unit.
        elif result.group('string'):
            word = cls.numeric_word_to_int(result.group('string'))
            if word is not None:
                countdown += word
        # Half unit.
        if result.group('half') or result.group('and'):
            countdown += 0.5
        # Unit type.
        if re.search('min', result.group('unit'), re.M | re.I):
            multiplier = 60
        else:
            multiplier = 1
        countdown = countdown * multiplier

        return countdown

    @staticmethod
    def numeric_word_to_int(word: str) -> Optional[int]:
        """
        Convert textual numbers into integers.

        :param word: Textual number from zero to nine

        :return: Number from 0 to 9, if any

        :todo: throw exception when word not found.
        """
        numbers = {
            0: 'zero',
            1: 'one',
            2: 'two',
            3: 'three',
            4: 'four',
            5: 'five',
            6: 'six',
            7: 'seven',
            8: 'eight',
            9: 'nine',
        }
        return next(
            (k for k, v, in numbers.items() if v == word.lower()), None
        )

    @staticmethod
    def countdown_to_time(
        number: Union[int, float], time_format: str = TIME_FORMAT
    ) -> str:
        """
        Convert a number of seconds to midnight into a time format.

        :param number: Number representing a countdown
        :param time_format: ``strftime()`` time format

        :return: Time representation of countdown to midnight
        """
        midnight = datetime.datetime.combine(
            datetime.date.today() + datetime.timedelta(days=1),
            datetime.time(0, 0, 0, 0),
        )
        minutes = number // 60
        seconds = number - minutes * 60
        delta = datetime.timedelta(minutes=minutes, seconds=seconds)

        return (midnight - delta).strftime(time_format)


class CountdoomClientError(Exception):
    """Countdoom client general error."""

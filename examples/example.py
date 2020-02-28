# -*- coding: utf-8 -*-

"""Usage examples for Countdoom."""

import asyncio
from typing import Dict, Union

from countdoom import CountdoomClient


def get_doomsday_clock() -> Dict[str, Union[str, float, None]]:
    """
    Get current Doomsday Clock value.

    :return: Dictionary of Doomsday Clock representation styles
    """
    client = CountdoomClient()
    loop = asyncio.get_event_loop()
    task = loop.create_task(client.fetch_data())
    data = loop.run_until_complete(task)
    return data


async def async_get_doomsday_clock() -> Dict[str, Union[str, float, None]]:
    """
    Get current Doomsday Clock value using AsyncIO.

    :return: Dictionary of Doomsday Clock representation styles
    """
    client = CountdoomClient()
    data = await client.fetch_data()
    return data

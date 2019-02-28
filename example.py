# -*- coding: utf-8 -*-

"""
Usage examples for Doomsday Py.
"""

import asyncio
from typing import Dict, Union

from doomsday_clock import DoomsdayClock


def get_doomsday_clock() -> Dict[str, Union[str, float]]:
    """
    Get current Doomsday Clock value.

    :return: Dictionary of Doomsday Clock representation styles
    """
    client = DoomsdayClock()
    loop = asyncio.get_event_loop()
    task = loop.create_task(client.fetch_data())
    data = loop.run_until_complete(task)
    return data


async def async_get_doomsday_clock() -> Dict[str, Union[str, float]]:
    """
    Get current Doomsday Clock value using AsyncIO.

    :return: Dictionary of Doomsday Clock representation styles
    """
    client = DoomsdayClock()
    data = await client.fetch_data()
    return data

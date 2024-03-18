#!/usr/bin/env python3
"""
0. The basics of async
"""

import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    asynchronously waits for a random amount of
    time up to a specified maximum delay.

    Args:
      max_delay (int): maximum amount of time (in seconds)
      Defaults to 10

    Returns:
      float value representing the delay that was randomly
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay

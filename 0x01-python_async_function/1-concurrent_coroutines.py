#!/usr/bin/env python3
"""
1. Let's execute multiple coroutines at the
same time with async
"""


import asyncio
from typing import List


wait_random = __import__("0-basic_async_syntax").wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Waits for a random delay multiple times and
    returns a sorted list of the delays.

    Args:
      n (int): The number of times to wait for a
        random delay.
      max_delay (int): The maximum delay value.

    Returns:
      List[float]: A sorted list of the delays.
    """
    delays = [await wait_random(max_delay) for _ in range(n)]
    return sorted(delays)

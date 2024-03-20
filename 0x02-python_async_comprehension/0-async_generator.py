#!/usr/bin/env python3

"""
0. Async Generator
"""


import asyncio
import random


async def async_generator() -> float:
    """
    The async_generator function asynchronously
    yields random numbers between 0 and 10 after
    a 1-second delay for each iteration.
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)

#!/usr/bin/env python3

"""
2. Run time for four parallel comprehensions
"""

import asyncio
from time import perf_counter

async_comprehension = __import__("1-async_comprehension").async_comprehension


async def measure_runtime() -> float:
    """
    Measures the runtime of executing four instances of
    the async_comprehension function concurrently.

    Returns:
      The total runtime in seconds.
    """
    start_time = perf_counter()
    await asyncio.gather(
        async_comprehension(),
        async_comprehension(),
        async_comprehension(),
        async_comprehension(),
    )
    end_time = perf_counter()
    return end_time - start_time

#!/usr/bin/env python3

"""
1. Async Comprehensions
"""


from typing import List


async_generator = __import__("0-async_generator").async_generator


async def async_comprehension() -> List[float]:
    """
    Async function that returns a list of floats.

    This function uses an async generator to generate
    a sequence of floats, and then uses an async
    comprehension to transform the generated sequence
    into a list of floats.

    Returns:
      A list of floats generated from the async generator.

    """
    return [i async for i in async_generator()]

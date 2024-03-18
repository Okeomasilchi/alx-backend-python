#!/usr/bin/env python3
"""
module that contains the function task_wait_random
"""

import asyncio
from asyncio import Task
from typing import TypeVar


wait_random = __import__("0-basic_async_syntax").wait_random


_T = TypeVar("_T")


def task_wait_random(max_delay: int) -> Task[_T]:
    """
    Create and return a task that waits for a random
    amount of time.

    Args:
      max_delay (int): The maximum delay in seconds.

    Returns:
      Task: A task that represents the asynchronous
      operation of waiting for a random amount of time.
    """
    return asyncio.create_task(wait_random(max_delay))

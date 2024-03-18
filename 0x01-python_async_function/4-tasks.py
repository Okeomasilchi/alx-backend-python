#!/usr/bin/env python3
"""
This module contains functions related to tasks.
"""

import asyncio
from typing import List


task_wait_random = __import__("3-tasks"
                              ).task_wait_random


async def task_wait_n(n: int,
                      max_delay: int
                      ) -> List[float]:
    """
    Executes multiple instances of the task_wait_random
    coroutine concurrently.

    Args:
      n (int): The number of tasks to execute.
      max_delay (int): The maximum delay for each task.

    Returns:
      List[float]: A list of floats representing the
      delays of each task.
    """
    tasks = [task_wait_random(max_delay) for _ in range(n)]
    return await asyncio.gather(*tasks)

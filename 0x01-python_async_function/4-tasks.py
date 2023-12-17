#!/usr/bin/env python3
"""Creates an asyncio task."""

# import asyncio
from typing import List

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """Calls wait_random @n times and passes @max_delay to it."""
    res = []
    for _ in range(n):
        sec = await task_wait_random(max_delay)
        res.append(sec)
    return res

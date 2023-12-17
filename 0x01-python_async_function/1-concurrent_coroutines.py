#!/usr/bin/env python3
"""
Running multiple routines
"""

from typing import List
import asyncio

wait_random = __import__("0-basic_async_syntax").wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """Calls wait_random @n times and passes @max_delay to it."""
    return await asyncio.gather(*(wait_random(max_delay) for _ in range(n)))

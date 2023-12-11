#!/usr/bin/env python3
"""
Running multiple routines
"""

import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n, max_delay):
    """Calls wait_random @n times and passes @max_delay to it."""
    res = []
    for i in range(n):
            sec = await wait_random(max_delay)
            res.append(sec)
    return res

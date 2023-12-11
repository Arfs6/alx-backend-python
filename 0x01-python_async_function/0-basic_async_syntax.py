#!/usr/bin/env python3
"""Basic asynch io syntax."""

import random as r
import asyncio


async def wait_random(max_delay=10):
    """Waits for a random number of seconds up to @max_delay."""
    delay = r.uniform(0, max_delay + 1)
    await asyncio.sleep(delay)
    return delay

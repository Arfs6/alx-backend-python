#!/usr/bin/env python3
"""Async and generators."""

from typing import Generator
import random
import asyncio


async def async_generator() -> Generator[int]:
    """Wait for 1 second and yield a random number."""
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.randint(0, 11)

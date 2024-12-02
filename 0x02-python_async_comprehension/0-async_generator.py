#!/usr/bin/env python3
"""generator created"""
import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """wais one second and give a random num"""
    for _ in range(0, 10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)

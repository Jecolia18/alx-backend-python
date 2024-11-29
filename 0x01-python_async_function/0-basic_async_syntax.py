#!/usr/bin/env python3
"""coroutine that takes an integer"""


import random
import asyncio


async def wait_random(max_delay: int = 10) -> float:
    """returns a number"""

    num = (random.uniform(0, max_delay))
    await asyncio.sleep(num)
    return num

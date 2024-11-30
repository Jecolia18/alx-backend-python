#!/usr/bin/env python3
""" measures the total execution time"""
import time
import asyncio
from typing import List


wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(max_delay: int = 10, n: int = 0) -> float:
    """ Args: 
    max_delay: max wait
    n: num function

    Return
    float
    """
    first = time.perf_counter()
    asyncio.run(wait_n(max_delay, n))
    elapsed = time.perf_counter() - first
    total_time = elapsed / n

    return total_time

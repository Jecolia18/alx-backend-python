#!/usr/bin/env python3
""""time measurement"""
import asyncio
import time
async_comprehension = __import('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """time measurement"""
    start_time = time.perf_counter()
    await asyncio.gather(async_comprehension(), async_comprehension(),
            async_comprehension(), async_comprehension())
    return time.perf_counter - start_time

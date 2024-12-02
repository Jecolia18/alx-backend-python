#!/usr/bin/ env python3
"""genereate a list """
from typing import List
async_generator = __import__('async_generator').async_generator


async def async_comprehension() -> List[float]:
    """return the generated list"""
    return [_ async for _ in async_generator()]

#!/usr/bin/env python3
"""a function that returns another function"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """returns a function that multiplies"""
    def mul(omg: float) -> float:
        """ the function to return"""
        return omg * multiplier
    return mul

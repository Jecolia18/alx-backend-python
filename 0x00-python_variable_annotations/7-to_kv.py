#!/usr/bin/env python3
"""function that returns a tuple"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """returns a tuple"""
    tup = k, float(v * v)
    return tuple(tup)

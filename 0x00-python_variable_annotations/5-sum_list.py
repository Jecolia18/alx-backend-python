#!/usr/bin/env python3
"""type-annotated function"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """funcions that returns the sum of a list"""
    su = 0
    for i in input_list:
        su += i
    return float(su)

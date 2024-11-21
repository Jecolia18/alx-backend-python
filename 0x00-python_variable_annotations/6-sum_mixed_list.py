#!/usr/bin/env python3
"""a function that does the sum"""
from typing import List, Union

def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """adds integers and floats"""
    return float(sum(mxd_lst))

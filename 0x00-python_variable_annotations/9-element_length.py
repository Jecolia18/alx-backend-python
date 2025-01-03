#!/usr/bin/env python3
"""annotation of function"""
from typing import List, Iterable, Sequence, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """annotation """
    return [(i, len(i)) for i in lst]

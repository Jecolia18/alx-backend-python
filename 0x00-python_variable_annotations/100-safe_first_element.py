#!/usr/bin/env python3
""" duck annotations """
from typing import Any, Sequence, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """duck typing"""
    if lst:
        return lst[0]
    else:
        return None

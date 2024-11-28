#!/usr/bin/env python3
"""advanced task type annotations"""
from typing import Any, Mapping, Union, TypeVar


T = TypeVar('T')
Res = Union[Any, T]
Def = Union[T, None]


def safely_get_value(dct: Mapping, key: Any, default: Def = None) -> Res:
    """getting a value from a dictionnary"""
    if key in dct:
        return dct[key]
    else:
        return default

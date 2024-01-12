#!/usr/bin/env python3
"""Type-annotated function module"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """Takes a string k and an int or float as second
       argument and returns a tuple.
       Parameters
       - k(str): a string element
       - v(Union[int, float])
    """
    return (k, v ** 2)

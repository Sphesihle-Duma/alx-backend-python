#!/usr/bin/env python3
"""type-annotated function module"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """Calculating the sum of the mixed element in a list"""
    sum: float = 0
    for input in mxd_lst:
        sum += input
    return sum

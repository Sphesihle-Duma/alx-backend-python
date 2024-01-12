#!/usr/bin/env python3
"""type-annotated function module"""
from typing import List


def sum_mixed_list(mxd_lst: List[int or float]) -> float:
    """Calculating the sum of the mixed element in a list"""
    sum: float = 0
    for input in mxd_lst:
        sum += input
    return sum

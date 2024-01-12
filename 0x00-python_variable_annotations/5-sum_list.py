#!/usr/bin/env python3
"""type-annotated function module"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """Calculating sum of float"""
    sum = 0
    for input in input_list:
        sum += input
    return sum

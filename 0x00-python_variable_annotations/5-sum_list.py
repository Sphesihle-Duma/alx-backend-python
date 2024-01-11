#!/usr/bin/python3
"""type-annotated function module"""


def sum_list(input_list: [float]) -> float:
    """Calculating sum of float"""
    sum = 0
    for input in input_list:
        sum += input
    return sum

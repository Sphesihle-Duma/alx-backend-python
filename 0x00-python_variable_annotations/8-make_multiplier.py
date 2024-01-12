#!/usr/bin/env python3
"""type-annotated function module"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Returning a function that multiplies float and float"""
    def final(x: float) -> float:
        """returns the of x and multiplier"""
        return x * multiplier
    return final

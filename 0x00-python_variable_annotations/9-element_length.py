#!/usr/bin/env python3
"""type-annotated functions module"""
from typing import List, Tuple


def element_length(lst: List[str]) -> List[Tuple[str, int]]:
    """Returning a list of Tuples"""
    return [(i, len(i)) for i:str in lst]

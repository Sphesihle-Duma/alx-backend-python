#!/usr/bin/env python3
"""type-annotated functions module"""
from typing import List, Tuple, Sequence, Iterable


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """Returning a list of Tuples"""
    return [(i, len(i)) for i in lst]

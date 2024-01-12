#!/usr/bin/env python3
"""A module that uses safety first element variables"""
from typing import Union, Sequence, Any


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """Returning the first element of lst if it exist"""
    if lst:
        return lst[0]
    else:
        return None

#!/usr/bin/env python3
"""type-annotated function module"""
from typing import TypeVar, Mapping, Any, Union

T = TypeVar('T')


def safely_get_value(
    dct: Mapping[Any, T],
    key: Any,
    default: Union[T, None]
) -> Union[Any, T]:
    """Checks if the key is in the dct; if so, return the value for the key,
    else return None.
    """
    if key in dct:
        return dct[key]
    else:
        return default

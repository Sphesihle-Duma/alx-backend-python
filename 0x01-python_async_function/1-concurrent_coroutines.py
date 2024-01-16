#!/usr/bin/env python3
"""Concurent functions module"""
import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """Running async functions concurently"""
    tasks = [wait_random(max_delay) for i in range(0, n)]
    result: List[float] = await asyncio.gather(*tasks)
    return sorted(result)

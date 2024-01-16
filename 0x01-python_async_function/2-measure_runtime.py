#!/usr/bin/env python3
"""Sum of delay time of the async function"""
import asyncio
from typing import List
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """Calculate the average time taken to a function"""
    fun_delay_n: List[float] = asyncio.run(wait_n(n, max_delay))
    return sum(fun_delay_n) / n

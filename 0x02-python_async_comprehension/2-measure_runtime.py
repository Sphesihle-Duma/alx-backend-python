#!/usr/bin/env python3
"""A module that runs async comprehension"""
import asyncio
import time
async_compr = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """Calculating the average time"""
    my_list = [async_compr() for i in range(4)]
    start_time = time.time()
    await asyncio.gather(*my_list)
    end_time = time.time()
    return end_time - start_time

#!/usr/bin/env python3
"""Concurent functions module"""
import asyncio
from typing import List
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """Running async functions concurently"""
    tasks = [task_wait_random(max_delay) for i in range(0, n)]
    result: List[float] = await asyncio.gather(*tasks)
    return sorted(result)

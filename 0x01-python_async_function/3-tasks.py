#!/usr/bin/env python3
"""Module for return async function"""
import asyncio
from typing import Awaitable
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    Returns an asynchronous task for wait_random.

    Args:
        max_delay (int): The maximum delay.

    Returns:
        asyncio.Task[float]: An asynchronous task.
    """
    return asyncio.create_task(wait_random(max_delay))

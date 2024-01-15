#!/usr/bin/env python3
"""Asynchronous module"""
from random import uniform
import asyncio


async def wait_random(max_delay: int = 10) -> float:
    """Returnin the delay in the async func"""
    delay = uniform(0, float(max_delay))
    await asyncio.sleep(delay)
    return delay

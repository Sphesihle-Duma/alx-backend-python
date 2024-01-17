#!/usr/bin/env python3
"""Async generator module"""
import asyncio
from typing import Generator
from random import uniform


async def async_generator() -> Generator[float, None, None]:
    """Yielding the float random numbers"""
    for i in range(0, 10):
        await asyncio.sleep(1)
        yield float(uniform(0, 10))

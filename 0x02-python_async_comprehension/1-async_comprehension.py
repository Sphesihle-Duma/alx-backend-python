#!/usr/bin/env python3
"""Implementing the generator function"""
import asyncio
from typing import List, Generator
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> Generator[List[float], None, None]:
    """Returning the list of floats"""
    return [i async for i in async_generator()]

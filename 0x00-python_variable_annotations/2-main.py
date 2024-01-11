#!/usr/bin/env python3
floor = __import__('2-floor').floor
import math
ans = floor(3.14)
print(ans == math.floor(3.14))
print(floor.__annotations__)
print(f"floor(3.14) return {ans}, which is a {type(ans)}")

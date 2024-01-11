#!/usr/bin/env python3
add = __import__('0-add').add
print(add(1.11, 2.22) == 1.11 + 2.22)
if isinstance(add(1.22, 2.33), float):
    print(f"{add(1.22, 2.33)} is a float")

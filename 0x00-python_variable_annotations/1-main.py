#!/usr/bin/env python3

concat = __import__('1-concat').concat

str1: str = "Egg"
str2: str = "shell"

print(f'{concat(str1, str2)} == {str1}{str2}')

#! /user/bin/env python
"""this is python teprurature
"""
def f_to_k(temp):
    converted = ((temp - 32) * (5/9.0)) + 273.15
    return converted

print(f_to_k(32))
print(f_to_k(212))

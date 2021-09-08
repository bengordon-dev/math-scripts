#!/usr/bin/env python3
def exp(x, n, s):
    t, y = 1, 1
    m = x/n
    for i in range(1, s+1):
        t *= (m/i)
        y += t
    t = 1
    for i in range(0, n):
        t *= y
    return t
print(exp(1, 10, 10))
import math
print(math.e)

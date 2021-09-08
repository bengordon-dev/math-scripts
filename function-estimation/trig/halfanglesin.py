#!/usr/bin/env python3
import itertools
def halfAngleExtend(f):
    def g(x):
        y = f(x/4)
        return 2*f(x/2)*(1 - 2*y*y)
    return g
def sins():
    f = lambda x: x - (x*x*x)/6 + (x*x*x*x*x)/120
    while True:
        yield f
        f = halfAngleExtend(f)
def sin(x, precision):
    return (next(itertools.islice(sins(), precision, None)))(x)
def cos(x, precision):
    y = sin(x/2.0, precision)
    return 1 - 2*y*y
print(sin(10, 5))
print(cos(10, 5))

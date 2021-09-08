#!/usr/bin/env python3
import matplotlib.pyplot as plt

def dubmap(x0, n):
    out = [x0]
    for x in range(0, n-1):
        xn = out[-1]
        out.append((2*xn) % 1)
    return out

def dubmapplt(x0, n, precision):
    plt.subplot(1, 2, 1)
    ys = dubmap(x0, n)
    xs = [x for x in range(0, n)]
    plt.scatter(xs, ys)

    plt.subplot(1, 2, 2)
    dic = {}
    for point in ys:
        mjr = int(point*precision)
        if mjr not in dic.keys():
            dic[mjr] = 1
        else:
            dic[mjr] += 1
    ys = list(dic.values())
    ys = [y/n for y in ys]
    xs = list(dic.keys())

    plt.scatter(xs, ys)

    plt.show()

while True:
    dubmapplt(float(input("x0 > ")), int(input("n > ")), int(input("precision > ")))

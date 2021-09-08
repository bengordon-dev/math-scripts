#!/usr/bin/env python3
acc = str(open("e.txt", "r").read())[:-1]
def fac(n):
    out, i = 1, 2
    while i <= n:
        out *= i
        i += 1
    return out

def est(s): # returns an integer fraction approximating e
    sfac = fac(s)   
    out = [sfac, sfac]
    t = out[0]
    for j in range(1, s+1):
        t //= j
        out[0] += t
    return out

def decimal(s, p): #takes in integers, returns a string
    frac = est(s)
    out = ""
    num, den = frac[0], frac[1]
    for x in range(p+1):
        if num//den == 0:
            num *= 10
        out += str(num//den)
        num -= ((num//den)*den)
    return out[0] + "." + out[1:]

def accuracy_test(s, p):
    calcd = decimal(s, p)
    accr = acc[:p+2]
    out = 0
    while calcd[out] == accr[out]:
        out += 1
    return out-2

def acc_decimal(s, maxp):
    decimals = accuracy_test(s, maxp)
    return decimal(s, decimals)


def acc_array(s1, s2,  maxp):
    out = []
    for s in range(s1, s2+1):
        out.append(accuracy_test(s, maxp))
    return out

from sys import argv as args
if len(args) > 1:
    print(acc_array(int(args[1]), int(args[2]), int(args[3])))
else:
    print(acc_array(1, 40, 150))

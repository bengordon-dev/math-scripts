#!/usr/bin/env python3
acc = str(open("e.txt", "r").read())[:-1]
def fac(n):
    out, i = 1, 2
    while i <= n:
        out *= i
        i += 1
    return out

def est(n, s): # returns an integer fraction approximating e
    nfac, sfac = fac(n), fac(s)   
    out = [sfac*(n**s), (sfac*(n**s))**n]
    t = out[0]
    for j in range(1, s+1):
        t //= (j*n)
        out[0] += t
    t = out[0]
    return [(out[0])**n, out[1]]

def decimal(n, s, p): #takes in integers, returns a string
    frac = est(n, s)
    out = ""
    num, den = frac[0], frac[1]
    for x in range(p+1):
        if num//den == 0:
            num *= 10
        out += str(num//den)
        num -= ((num//den)*den)
    return out[0] + "." + out[1:]

def accuracy_test(n, s, p):
    calcd = decimal(n, s, p)
    accr = acc[:p+2]
    out = 0
    while calcd[out] == accr[out]:
        out += 1
    return out-2

def acc_decimal(n, s, maxp):
    decimals = accuracy_test(n, s, maxp)
    return decimal(n, s, decimals)


def acc_array(s1, s2, n1, n2, maxp):

    array = []
    for s in range(s1-1, s2):
        array.append([])
        for n in range(n1, n2+1):
            array[-1].append(accuracy_test(n, s+1, maxp))

    l = len(str(max(array[-1])))+1
    for r in range(0, len(array)):
        array[r] = str(array[r]).replace("[", "").replace("]", "").split(",")
        for c in range(0, len(array[r])):
                if len(array[r][c]) < l:
                    array[r][c] = " "*(l - len(array[r][c])) + array[r][c]
                array[r][c] = array[r][c][1:]
    for r in array:
        print(str(r).replace("'", "").replace("[", "").replace("]", "").replace(",", ""))
from sys import argv as args
if len(args) > 1:
    acc_array(int(args[1]), int(args[2]), int(args[3]), int(args[4]), int(args[5]))
else:
    acc_array(1, 40, 1, 40, 150)

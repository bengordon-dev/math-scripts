#!/usr/bin/env python3
import random
def rule_30(l, c, r):
    return l ^ (c | r)
def int_rep(bits):
    out = 0
    for x in range(0, len(bits)):
        out += bits[len(bits) - x - 1]*(2**x)
    return out
def next_bit(bits, i):
    if i >= len(bits):
        raise ValueError
    if len(bits) < 3:
        return next_bit([0] + bits + [0])
    if i == 0:
        return rule_30(bits[-1], bits[i], bits[i+1])
    if i == len(bits) - 1:
        return rule_30(bits[i-1], bits[i], bits[0])
    return rule_30(bits[i-1], bits[i], bits[i+1])
def next_row(bits):
    return [next_bit(bits, i) for i in range(0, len(bits))]
def print_bits(bits):
    for bit in bits:    
        print(f"\033[38;5;{16 + 5*36}m[]" if bit == 1 else "\x1b[0;0m  ", end="")
    print("\x1b[0;0m")
def print_rows(bits, iterations):
    for i in range(0, iterations):
        print_bits(bits)
        bits = next_row(bits)
def central_columns(bits, iterations):
    out = ""
    for x in range(0, iterations):
        out += str(bits[len(bits)//2])
        bits = next_row(bits)
    return out
def int_reps(bits, iterations):
    for i in range(0, iterations):
        print(int_rep(bits))
        bits = next_row(bits)
def period_check(bits):
    i, nums = 0, {}
    while True:
        n = int_rep(bits)
        if n in nums.keys():
#            print(f"{n} occured at row {i}")
 #           print(f"{n} also occured at row {nums[n]}")
            return i - nums[n]
        nums[n] = i
        bits = next_row(bits)
        i += 1
def get_bit(x, length, index):
    return (x & (1 << (length-index))) >> (length - index)
def list_rep(x, length):
    out = []
    for i in range(1, length+1):
        out.append(get_bit(x, length, i))
    return out
def next_int(x, length):
    return int_rep(next_row(list_rep(x, length)))
def next_int_pure(x, length):
    out = rule_30(get_bit(x, length, length-1), get_bit(x, length, length), get_bit(x, length, 1))  
    for i in range(2, length):
        out += rule_30(get_bit(x, length, i-1), get_bit(x, length, i), get_bit(x, length, i+1)) << length-i
    return out + (rule_30(get_bit(x, length, length), get_bit(x, length, 1), get_bit(x, length, 2)) << length-1)


#init = random.randint(0, 0xffffff)
init = 0xfda272
for i in range(0, 100):
    print(init, hex(init), next_int_pure(init, 24))
    init = next_int(init, 24)


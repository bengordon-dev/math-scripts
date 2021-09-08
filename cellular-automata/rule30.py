#!/usr/bin/env python3
def rule_30(l, c, r):
    return l ^ (c | r)
def next_row(bitstring):
    s = "00" + bitstring + "00"
    out = ""
    for i in range(0, len(s) - 2):
        out += str(rule_30(int(s[i]), int(s[i+1]), int(s[i+2])))
    return out
def print_bitstring(s, offset):
    print("  "*offset, end="") 
    for c in s:    
        print(f"\033[38;5;{16 + 5*36}m[]" if c == "1" else "\x1b[0;0m  ", end="")
    print(" "*offset + "\x1b[0;0m")
def print_rows(n):
    init = "1"
    print_bitstring(init, n)
    for i in range(1, n):
        init = next_row(init)
        print_bitstring(init, n-i)
def central_columns(n):
    out = ""
    init = "1"
    for x in range(0, n):
        out += init[len(init)//2]
        init = next_row(init)
    return out
print_rows(15)
print(central_columns(1500))

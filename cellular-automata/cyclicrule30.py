#/usr/bin/env python3
def rule_30(l, c, r): # takes 3 bits, outputs 1
    return l ^ (c | r)
def get_bit(x, length, index): # indices range from 1 to length inclusive going from left to right
    return (x & (1 << (length-index))) >> (length - index) # and the number with a number only containing a 1 at the relevant index, then shift the bit to the rightmost position
def next_int(x, length):
    out = rule_30(get_bit(x, length, length-1), get_bit(x, length, length), get_bit(x, length, 1)) # cyclic rule - the right neighbor of the last bit is the first bit
    for i in range(2, length):
        out += rule_30(get_bit(x, length, i-1), get_bit(x, length, i), get_bit(x, length, i+1)) << length-i
    return out + (rule_30(get_bit(x, length, length), get_bit(x, length, 1), get_bit(x, length, 2)) << length-1) # cyclic rule - the left neighbor of the first bit is the left bit
def period_check(n, length):
    i, nums = 0, {}
    while True:
        if n in nums.keys():
            return i - nums[n]
        nums[n] = i
        n = next_int(n, length)
        i += 1
def better_hex(color):
    out = hex(color)[2:]
    return "#" + "0"*(6 - len(out)) + out 

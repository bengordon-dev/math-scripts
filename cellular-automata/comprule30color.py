#/usr/bin/env python3
from tkinter import Tk, Canvas

def rule_30(l, c, r): # takes 3 bits, outputs 1
    return l ^ (c | r)

def get_bit(x, length, index): # indices range from 1 to length inclusive going from left to right
    return (x & (1 << (length-index))) >> (length - index) # and the number with a number only containing a 1 at the relevant index, then shift the bit to the rightmost position

def next_int(x, length):
    out = rule_30(get_bit(x, length, length-1), get_bit(x, length, length), get_bit(x, length, 1)) # cyclic rule - the right neighbor of the last bit is the first bit
    for i in range(2, length):
        out += rule_30(get_bit(x, length, i-1), get_bit(x, length, i), get_bit(x, length, i+1)) << length-i # left, current, right
    return out + (rule_30(get_bit(x, length, length), get_bit(x, length, 1), get_bit(x, length, 2)) << length-1) # cyclic rule - the left neighbor of the first bit is the left bit

def better_hex(color): #ensures valid 24-bit hex colors
    out = hex(color)[2:]
    return "#" + "0"*(6 - len(out)) + out 

def update(init, canvas, r, root):
    canvas.itemconfig(r, fill=better_hex(init), outline=better_hex(init))
    init = next_int(init, 24)
    root.after(1000, lambda: update(init, canvas, r, root))

root = Tk()
canvas = Canvas()
init = 0xfda272 #any 24-bit number should work except 0x000000, 0xffffff,0xaaaaaa, 0x555555, and anything that leads to it. Other numbers should give period 185040 cycles.
r = canvas.create_rectangle(0, 0, 100, 100, outline=better_hex(init), fill=better_hex(init))
canvas.pack()
update(init, canvas, r, root)
root.geometry("100x100")
root.mainloop()

from tkinter import Tk, Canvas, BOTH
import cyclicrule30 as cyclic
import time

def update(init, canvas, r, root):
    canvas.itemconfig(r, fill=cyclic.better_hex(init))
    init = cyclic.next_int(init, 24)
    root.after(1000, lambda: update(init, canvas, r, root))

root = Tk()
canvas = Canvas()
init = 0xfda272
r = canvas.create_rectangle(30, 10, 120, 80, outline="#fb0", fill="#fda272")
canvas.pack(fill=BOTH, expand=1)
update(init, canvas, r, root)
root.geometry("400x100+300+300")
root.mainloop()

import random
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

large_font = ('Verdana',30)

top = tk.Tk()
top.title(string="Role the Dice!!!")

def callback():
	dice_num = random.randint(1, 6)
	v.set(dice_num)


lb_1 = tk.Label(top, text="Let's Play...")
lb_1.grid(row=0, column=0)

ttk.Style().configure('blue/black.TButton', foreground='blue', background='black')
b1 = ttk.Button(top, text="Role the Dice!", style='blue/black.TButton', command=lambda: callback())
b1.grid(row=1, column=0)

v = tk.StringVar()
E1 = tk.Entry(top, width=1, textvariable=v, font=large_font, bd=5)
E1.grid(row=1, column=1)


top.mainloop()


#width=22, height=12



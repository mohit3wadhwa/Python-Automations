from tkinter import *
import tkinter.messagebox
import tkinter

top = Tk()
L1 = Label(top, text="Enter first Number")
E1 = Entry(top, bd =5)
L2 = Label(top, text="Enter second Number")
E2 = Entry(top, bd =5)

E1.pack(side = RIGHT)
L1.pack( side = LEFT)
E2.pack(side = RIGHT)
L2.pack( side = LEFT)


def CalculateSum(a,b):
	c = a + b
	var = StringVar()
	label = Label( root, textvariable=var, relief=RAISED )
	var.set(c)
	label.pack()
   

B = tkinter.Button(top, text ="Calculate", command = CalculateSum(E1,E2))

B.pack()

top.mainloop()


from Tkinter import *

def print_msg():
    a=E1.get()
    b=E2.get()
    print int(a)+int(b)

top = Tk()
L1 = Label(top, text="ENTER NUMBERS ")
L1.pack()
E1 = Entry(top, bd =5)
E1.pack()
E2 = Entry(top, bd =2)
E2.pack()
b1 = Button(top, text="submit",command=print_msg)
b1.pack()

top.mainloop()

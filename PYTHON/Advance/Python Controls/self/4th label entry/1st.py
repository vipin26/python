from Tkinter import *

c=0
def print_msg():
    a=E1.get()
    b=E2.get()
    c=int(a)+int(b)
    E3.insert(0,str(c))
    
top = Tk()
L1 = Label(top, text="ENTER NUMBERS ")
L1.pack()
E1 = Entry(top, bd =5)
E1.pack()
E2 = Entry(top, bd =2)
E2.pack()
b1 = Button(top, text="submit",command=print_msg)
b1.pack()
E3= Entry(top,bd=5)
E3.pack()

top.mainloop()

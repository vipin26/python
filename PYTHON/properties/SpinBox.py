from Tkinter import *

top = Tk()
top.geometry("200x80")
sb = Spinbox(top, from_=10, to=100,activebackground="blue",bd=1,cursor="circle",bg="green",fg="brown",font=("times new roman",50,"bold"))
sb.pack()
top.mainloop()

from Tkinter import *

top = Tk()
top.geometry("300x150")
sc = Scale(top,cursor="circle",from_=50,to=200,activebackground="blue",bg="red",orient=VERTICAL)
sc.pack(fill=X)

top.mainloop()

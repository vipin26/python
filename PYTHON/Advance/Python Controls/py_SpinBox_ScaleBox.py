from Tkinter import *
import tkMessageBox

top = Tk()

def show():
   tkMessageBox.showinfo("Spin Box value ","Value from Spin Box "+str(sb.get()))
   tkMessageBox.showinfo("Scale Value ","Value from Scale Box "+str(sc.get()))

sb = Spinbox(top, from_=0, to=10)
sb.pack()

sc = Scale(top,orient=HORIZONTAL)
sc.pack()

b1=Button(top,text="Click me ", width="20",height="5",command=show)
b1.pack()

top.mainloop()

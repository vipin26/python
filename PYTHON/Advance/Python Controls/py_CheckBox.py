from Tkinter import *
import tkMessageBox
import Tkinter

top = Tkinter.Tk()
CheckVar1 = IntVar()
CheckVar2 = IntVar()

def show():
   a=""
   if(CheckVar1.get()==1):
      a=a+" Programming"
   if(CheckVar2.get()==1):
      a=a+" Sports"
   tkMessageBox.showinfo("Selected values ",a)
 


C1 = Checkbutton(top, text = "Programming ", variable = CheckVar1, onvalue = 1, offvalue = 0, height=5, width = 20)
C2 = Checkbutton(top, text = "Sports ", variable = CheckVar2, onvalue = 1, offvalue = 0, height=5, width = 20)
C1.pack()
C2.pack()
b=Button(top,text="click here",command=show)
b.pack()
top.mainloop()

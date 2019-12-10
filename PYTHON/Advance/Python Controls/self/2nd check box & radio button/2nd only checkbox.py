from Tkinter import *
import tkMessageBox
import Tkinter

top=Tkinter.Tk()
CheckVar1=IntVar()
CheckVar2=IntVar()

def school():
    a=""
    if(CheckVar1.get()==1):
        a=a+"staff "
    print a
    if(CheckVar2.get()==1):
        a=a+"student "
    print a
    tkMessageBox.showinfo("Title ",a)

C1=Checkbutton(top,text="staff",variable=CheckVar1,onvalue=1,offvalue=0,height=5,width=20)
C1.pack()
C2=Checkbutton(top,text="student",variable=CheckVar2,onvalue=1,offvalue=0,height=5,width=20)
C2.pack()
b=Button(top,text="click here",command=school)
b.pack()

top.mainloop()

from Tkinter import *
import Tkinter

top=Tkinter.Tk()
top.geometry("500x500")

var = IntVar()

L5=Label(text="GENDER")
L5.place(x=10,y=200,height=30,width=100)

rb1=Radiobutton(top,text="Male",variable=var,value=1)
rb1.place(x=120,y=200,height=30,width=50)

rb2=Radiobutton(top,text="Female",variable=var,value=2)
rb2.place(x=200,y=200,height=30,width=50)

top.mainloop()

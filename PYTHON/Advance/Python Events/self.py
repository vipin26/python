from Tkinter import *
import tkMessageBox

def left(event):
    print"left button"
def right(event):
    print"right button"
def enter(event):
    print"Enter Event"
def out(event):
    Top.geometry("300x300")

Top=Tk()
B1=Button(Top,text="Button")
B1.pack()
B1.bind('<Button-1>',left)
B1.bind('<Button-2>',right)
Top.bind('<Shift_L>',enter)
Top.bind('<Configure>',out)

Top.mainloop()

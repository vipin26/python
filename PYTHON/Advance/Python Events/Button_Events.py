from Tkinter import *
import tkMessageBox

def hello(event):
    print("Single Click, Button-l") 
def quit(event):                           
    print("Double Click, so let's stop") 
def in_focus(event):
    print("Enter Event ")
def out_focus(event):
    print("Leave Event ")
def key_event(event):
    print("You Pressed Enter Key ")
def right_click(event):
    print("You Pressed Right Click ")
def middle_click(event):
    print("You Pressed Mouse Wheel ")
def scroll_up(event):
    print("You Pressed Mouse Wheel ")
    
top = Tk()

B1 = Button(top, text='Mouse Clicks')
B1.pack()
B1.bind('<Button-1>', hello)
#top.bind('<Button-2>', middle_click)
#top.bind('<Button-3>', right_click)
#top.bind('<Button-4>', scroll_up)

B1.bind('<Double-1>', quit)
B1.bind('<Enter>', quit)
top.bind('<Enter>', in_focus)
top.bind('<Leave>', out_focus)
top.bind('<Tab>', key_event)


top.mainloop()

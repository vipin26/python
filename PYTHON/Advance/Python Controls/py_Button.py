from Tkinter import *

def callback():
    print "clicked!"
    print T.get("1.0",END)

L1=Label(text="Enter Ur Name ")
L1.pack()
T = Text(height=2, width=30)
T.pack()

b = Button(text="click me", command=callback)
b.pack()

mainloop()

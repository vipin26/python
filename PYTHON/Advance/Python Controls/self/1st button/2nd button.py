from Tkinter import *

def addition():
    print "clicked"
    a=int(T1.get("1.0",END))
    b=int(T2.get("1.0",END))
    T3.insert(END,str(a+b))
    #print T3.get("1.0",END)
L1=Label(text="Enter First Number ")
L1.pack()
T1=Text(height=2,width=30)
T1.pack()
L2=Label(text="Enter Second Number ")
L2.pack()
T2=Text(height=2,width=30)
T2.pack()

b=Button(text="click me", command=addition)
b.pack()

L3=Label(text="sum is ")
L3.pack()
T3=Text(height=2,width=30)
T3.pack()

mainloop()
